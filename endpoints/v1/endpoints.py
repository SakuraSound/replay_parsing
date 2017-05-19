from datetime import datetime

import uuid
import traceback
import sanic

import bson
import pymongo

from replays.starcraft.replay import Replay as SC2Replay

import swift

STARCRAFT = 'starcraft'

GAMES = [STARCRAFT]


async def accept_replay(request, game):
    """
     Take replay file from request
     Extract basic information about replay
     Return information to client or tell client data is invalid
    """
    game = game.lower()
    replay_file = request.files.get('replay')
    if replay_file:
        if game == STARCRAFT:
            load_map = request.args.get("load_map", False)
            result = await SC2Replay.analyze_replay(replay_file, load_map)
            if result:
                data = {"result": result,
                        "game": STARCRAFT,
                        "success": True}
                return sanic.response.json(data, status=200)
            else:
                data = {
                    "error": "Unable to parse game file.",
                    "success": False,
                    "game": game
                }
                return sanic.response.json(data, status=500)
        else:
            data = {
                "error": "Game not in list of games.",
                "success": False,
                "game": game
            }
            return sanic.response.json(data, status=404)
    else:
        data = {
            "error": "No replay file given.",
            "success": False,
            "game": game
        }
        return sanic.response.json(data, status=500)


async def parse_replay(request, game):
    """
    Take replay file that was uploaded to ObjectStore and
    process data and store it to database and link to account
    """

    game = game.lower()
    replay_file = request.files.get("replay")
    if replay_file:
        if game == STARCRAFT:
            basic, result = await SC2Replay.process_replay(replay_file, request.args.get("load_map", False))
            if result:
                # Lets create our db entry

                basic['private_replay'] = request.args.get('private_replay', False)
                replay_id = str(uuid.uuid4())
                basic["_id"] = replay_id
                print(replay_id)
                unique_name = ".".join([replay_id, "SC2Replay"])
                basic["replay_object_name"] = unique_name
                basic["game_name"] = request.args.get("replay_name", datetime.utcnow())
                try:
                    success = await request.app.object_storage.add_object(request.app.config.OS_CONTAINER, replay_file, unique_name)
                    if success:
                        # push results to mongoDB
                        mongo = request.app.mongodb
                        # Insert the basic information for the replay
                        await mongo.starcraft_2_replays.info.insert_one(basic)
                        # Insert event data
                        events = dict(result['event'])
                        events.update(basic)
                        print(events)
                        await mongo.starcraft_2_replays.replay_events.insert_one(events)
                        # Insert stats data
                        stats = dict(result['stats'])
                        stats.update(basic)
                        await mongo.starcraft_2_replays.replay_stats.insert_one(stats)

                    return sanic.response.json(basic)
                except (swift.BluemixSwiftUnavailableError,
                        swift.BluemixSwiftAuthenticationError,
                        swift.BluemixSwiftRequestTimeoutError,
                        bson.errors.InvalidDocument,
                        pymongo.errors.ConnectionFailure):

                    traceback.print_exc()
                    data = {
                        "error": "Internal Server Error",
                        "success": False,
                        "game": STARCRAFT
                    }
                    return sanic.response.json(data)


async def get_replay(request, game, name):
    async def stream(response):
        async for data, byte_size in request.app.object_storage.get_object(request.app.config.OS_CONTAINER, name):
            if data:
                await response.write(data)
            else:
                break
    try:
        return await sanic.response.stream(stream, content_type="application/octet-stream")
    except swift.BluemixSwiftResourceNotFoundError:
        return await sanic.response.json({}, status=404)
        # add more exceptions


async def get_replays(request):
    pass


async def health(request):
    # Ping object storage
    # Ping cloudant

    pass
