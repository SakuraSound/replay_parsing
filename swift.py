import asyncio
import aiohttp
import io
import json
import math


class BluemixConnectionError(Exception):
    def __init__(self, message):
        self.message = message


class BluemixSwiftUnavailableError(Exception):
    def __init__(self, message):
        self.message = message


class BluemixSwiftResourceNotFoundError(Exception):
    def __init__(self, message):
        self.message = message


class BluemixSwiftRequestTimeoutError(Exception):
    def __init__(self, message):
        self.message = message


class BluemixSwiftAuthenticationError(Exception):
    def __init__(self, message):
        self.message = message


class BluemixSwift:

    def __init__(self, app):
        self.__token_url = "https://identity.open.softlayer.com/v3/auth/tokens"
        self.app = app

    @classmethod
    async def init_bluemix_swift_object(cls, app):
        swift = BluemixSwift(app)
        if not await swift.__get_token_and_url():
            # failure to connect
            raise BluemixConnectionError("Unable to connect to authentication service.")

        return swift

    @classmethod
    def init_bluemix_swift_object_sync(cls, app, loop=None):
        if not loop:
            loop = asyncio.get_event_loop()
        return loop.run_until_complete(cls.init_bluemix_swift_object(app))

    async def get_object_list(self, container, limit=100, marker=None):
        if self.__cant_connect():
            raise BluemixConnectionError("Token and URL required to connect to Bluemix Object Storage.")
        else:
            return await self.__get_objects_list(container, limit, marker)

    async def get_object(self, container, name):
        if self.__cant_connect():
            raise BluemixConnectionError("Token and URL required to connect to Bluemix Object Storage.")
        else:
            async for data, size in self.__get_object(container, name):
                yield(data, size)
                asyncio.sleep(0)

    async def add_object(self, container, obj, name):
        if self.__cant_connect():
            raise BluemixConnectionError("Token and URL required to connect to Bluemix Object Storage.")
        else:
            return await self.__add_object(container, obj, name)

    async def ping(self, container):
        # Just pings the container for the top entry
        return len(await self.get_object_list(container, limit=1)) == 1


    def __can_connect(self):
        return self.token and self.swift_url

    def __cant_connect(self):
        return not (self.token and self.swift_url)

    def __get_auth_header(self):
        return {'x-auth-token': self.token, 'accept': 'application/json'}

    def __get_token_payload(self):
        payload = {
            'auth': {
                'identity': {
                    'methods': ['password'],
                    'password': {
                        'user': {
                            'name': self.app.config.OS_USERNAME,
                            'domain': {
                                'id': self.app.config.OS_DOMAIN_ID},
                            'password': self.app.config.OS_PASSWORD}}}}}

        header = {'Content-Type': 'application/json'}
        return payload, header

    async def __get_swift_url(self, body):
        for entry in body['token']['catalog']:
            if entry['type'] == 'object-store':
                for endpoint in entry['endpoints']:
                    if endpoint['interface'] == 'public' and endpoint['region'] == self.app.config.OS_REGION:
                        return endpoint['url']

        raise BluemixSwiftUnavailableError("User not authorized for specified Bluemix Object Storage. Check services or if OS_REGION is correct.")

    async def __get_token_and_url(self):
        async with aiohttp.ClientSession() as session:
            payload, headers = self.__get_token_payload()
            async with session.post(self.__token_url, data=json.dumps(payload), headers=headers) as resp:
                if resp.status == 201:
                    self.token = resp.headers.get('x-subject-token')
                    self.swift_url = await self.__get_swift_url(await resp.json())
                    self.app.logger.info("Object Storage authentication successful.")
                    return True
                elif resp.status == 401:
                    # Unauthorized
                    self.app.logger.critical("Object Storage authentication unauthorized.")
                    raise BluemixSwiftUnavailableError("Unauthorized request.")
                elif resp.status == 403:
                    # Forbidden
                    self.app.logger.critical("Object Storage authentication access not allowed.")
                    raise BluemixSwiftUnavailableError("Requested authentication not allowed.")
                elif resp.status == 404:
                    # Not found
                    self.app.logger.critical("Object Storage authentication endpoint given does not exist.")
                    raise BluemixConnectionError("Requested authentication endpoint does not exist.")

    async def __get_objects_list(self, container, limit=None, marker=None):
        async with aiohttp.ClientSession() as session:
            params = {"format": "json"}
            self.__validate_and_add_parameter(limit, 'limit', int, params, min_val=0, max_val=100)
            self.__validate_and_add_parameter(marker, 'marker', str, params)
            url = "/".join([self.swift_url, container])
            async with session.get(url, headers=self.__get_auth_header(), params=params) as resp:
                if resp.status == 200:
                    objects = await resp.json()
                    self.app.logger.debug("Object List: container: '{0}' count: {1} limit: {2}  marker: {3}".format(container, len(objects), limit, str(marker)))
                    return objects
                elif resp.status == 204:
                    # No content...
                    self.app.logger.debug("Object List: container: {0} count: 0 limit: {1} marker: {2}".format(container, limit, str(marker)))
                    return []
                elif resp.status == 404:
                    self.app.logger.debug("Object List Found: container: {0} ".format(container))
                    raise BluemixSwiftResourceNotFoundError("Container requested does not exist.")

    async def __add_object(self, container, obj, name, expire_at=None):
        """

        """
        async with aiohttp.ClientSession() as session:
            url = "/".join([self.swift_url, container, name])
            headers = self.__get_auth_header()
            if expire_at:
                headers['x-delete-at'] = expire_at
            fields = {"file": obj}
            async with session.put(url, data=fields, headers=self.__get_auth_header()) as resp:
                if resp.status == 201:
                    # Created
                    self.app.logger.debug("Object Added: container: {0} name: {1}".format(container, name))
                    return True
                elif resp.status == 408:
                    # TimedOut
                    self.app.logger.debug("Object Add Timeout: container: {0} name: {1}".format(container, name))
                    raise BluemixSwiftRequestTimeoutError("Timed out trying to add object.")

    async def __get_object(self, container, name, chunk_size=262144):
        # Retrieve object as an asynchronous generator
        async with aiohttp.ClientSession() as session:
            url = "/".join([self.swift_url, container, name])
            async with session.get(url, headers=self.__get_auth_header()) as resp:
                size_bytes = 0
                if resp.status == 200:
                    self.app.logger.debug("Streaming Object: container: {0} name: {1}".format(container, name))
                    while True:
                        chunk = await resp.content.read(chunk_size)
                        if not chunk:
                            self.app.logger.debug("Object Retrieved: container: {0} name: {1}: total_size: {2} KB".format(container, name, math.ceil(size_bytes / 1024)))
                            yield None, size_bytes
                            await asyncio.sleep(0)
                            break
                        else:
                            self.app.logger.debug("Streaming Object: current_bytes: {0}".format(str(size_bytes)))
                            size_bytes += len(chunk)
                            yield chunk, size_bytes
                            await asyncio.sleep(0)
                elif resp.status == 401:
                    self.app.logger.debug("Authentication Error: Request not authenticated.")
                    raise BluemixSwiftAuthenticationError("Request was not authenticated. Check if token is valid.")
                elif resp.status == 404:
                    self.app.logger.debug("Object Not Found: container: {0} name: {1}".format(container, name))
                    raise BluemixSwiftResourceNotFoundError("Object with name '{0}' not found at given container '{1}'".format(name, container))


    def __validate_and_add_parameter(self, parameter, name, typ, dest, min_val=None, max_val=None):
        if parameter:
            if type(parameter) is typ:
                # Check if comparable...
                    if min_val:
                        if min_val > parameter:
                            raise ValueError("Parameter '{0}' is less than the min value '{1}'.".format(parameter, min_val))
                    if max_val:
                        if max_val < parameter:
                            raise ValueError("Parameter '{0}' is greater than the min value '{1}'.".format(parameter, min_val))
                    # All Good!
                    dest[name] = parameter
            else:
                raise TypeError("Parameter '{0}' should be of type '{1}'".format(name, str(typ)))




async def test(app):
    swift = await BluemixSwift.init_bluemix_swift_object(app)
    print(await swift.ping("StarcraftreplaysprojectforInterconnect2017"))
    print(await swift.get_object_list("StarcraftreplaysprojectforInterconnect2017", limit=2))

    byte = io.BytesIO()
    size = 0
    async for data, byte_size in swift.get_object("StarcraftreplaysprojectforInterconnect2017", '5ef5f2922631c04e04f066cce5f4d44d78004550.SC2Replay'):
        if data:
            byte.write(data)
            size = byte_size
        else:
            size = byte_size
            break

    print("Size of {0}".format("5ef5f2922631c04e04f066cce5f4d44d78004550.SC2Replay"), size)

if __name__ == '__main__':
    import logging
    import os
    import sys

    app = type('dummy_app', (), {})()
    app.config = type('dummy_config', (), {})()
    app.config.OS_PROJECT = os.environ.get("OS_PROJECT")
    app.config.OS_PROJECT_ID = os.environ.get("OS_PROJECT_ID")
    app.config.OS_REGION = os.environ.get("OS_REGION")
    app.config.OS_USER_ID = os.environ.get("OS_USER_ID")
    app.config.OS_USERNAME = os.environ.get("OS_USERNAME")
    app.config.OS_PASSWORD = os.environ.get("OS_PASSWORD")
    app.config.OS_DOMAIN_ID = os.environ.get("OS_DOMAIN_ID")
    app.config.OS_DOMAIN_NAME = os.environ.get("OS_DOMAIN_NAME")
    app.config.OS_VERSION = os.environ.get("OS_VERSION")
    app.config.OS_ROLE = os.environ.get("OS_ROLE")

    app.logger = logging.getLogger('app')
    app.logger.setLevel(logging.DEBUG)
    app.logger.addHandler(logging.StreamHandler(sys.stdout))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(app))
