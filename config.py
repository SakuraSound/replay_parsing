import errno
import logging
import os

import motor.motor_asyncio
from pymongo.errors import ConnectionFailure


import swift
from swift import BluemixSwift


ENV_VARS = ["DEBUG",
            "MONGODB_HOST",
            "MONGODB_CA_CERT",
            "OS_PROJECT",
            "OS_PROJECT_ID",
            "OS_REGION",
            "OS_USER_ID",
            "OS_USERNAME",
            "OS_PASSWORD",
            "OS_DOMAIN_ID",
            "OS_DOMAIN_NAME",
            "OS_CONTAINER",
            "OS_ROLE",
            "OS_VERSION",
            ]


async def setup_os_swift(app):
    try:
        app.object_storage = await BluemixSwift.init_bluemix_swift_object(app)
        app.logger.info("Retrieved authentication token for Object Storage service.")
    except swift.BluemixConnectionError:
        app.logger.critical("Unable to reach Object Storage service. Exiting")
        exit(errno.ENOTCONN)


async def setup_mongo(app):
    app.logger.info("Setting up connection to MongoDB.")
    try:
        client = motor.motor_asyncio.AsyncIOMotorClient(app.config.MONGODB_HOST,
                                                        ssl=True,
                                                        ssl_ca_certs=app.config.MONGODB_CA_CERT)

        app.mongodb = client
        app.logger.info("Successfully connected to MongoDB store")
    except ConnectionFailure:
        app.logger.critical("Unable to connect to MongoDB store. Exiting.")
        exit(errno.ENOTCONN)


def extract_env(app):
    env_vars = [os.environ.get(v, None) for v in ENV_VARS]
    if not all(env_vars):
        missing = [ENV_VARS[i] for i, flag in enumerate(env_vars) if not flag]
        return False, missing
    app.config.update({k: v for k, v in zip(ENV_VARS, env_vars)})
    return True, None


async def config(app, loop):
    result, flag = extract_env(app)
    if result:
        setup_logging(app)
        await setup_os_swift(app)
        await setup_mongo(app)
    else:
        logging.critical("Missing following: {0}".format(", ".join(flag)))
        exit()


def setup_logging(app):
    logging_format = "[%(asctime)s] %(process)d-%(levelname)s "
    logging_format += "%(module)s::%(funcName)s():l%(lineno)d: "
    logging_format += "%(message)s"

    logging.basicConfig(
        format=logging_format,
        level=logging.DEBUG if app.config.DEBUG is "1" else logging.INFO)

    app.logger = logging.getLogger()
