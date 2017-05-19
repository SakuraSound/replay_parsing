import asyncio
import io
import json
import traceback
from collections import defaultdict
from datetime import datetime

import sc2reader.engine
from sc2reader.engine.plugins import APMTracker, ContextLoader, SelectionTracker
from sc2reader.events import PlayerStatsEvent, UnitBornEvent, UnitInitEvent, UnitDoneEvent, UnitDiedEvent, UnitTypeChangeEvent, UpgradeCompleteEvent, TargetPointCommandEvent

from replays.starcraft.event_handling import unit_born, unit_done, unit_died, unit_type_change, upgrade_complete, player_stats, target_ability, default, unit_init


class Replay:

    __event_parsing__ = {
        UnitBornEvent: unit_born,
        UnitDoneEvent: unit_done,
        UnitDiedEvent: unit_died,
        UnitTypeChangeEvent: unit_type_change,
        UpgradeCompleteEvent: upgrade_complete,
        PlayerStatsEvent: player_stats,
        TargetPointCommandEvent: target_ability,
        UnitInitEvent: unit_init
    }

    __use_cache__ = frozenset([UnitBornEvent, UnitDoneEvent, UnitDiedEvent, UnitInitEvent])

    @classmethod
    def __give_cache(cls, event, cache):
        return cache if type(event) in cls.__use_cache__ else None

    @classmethod
    def get_plugins(cls):
        return [ContextLoader(), APMTracker(), SelectionTracker()]

    @classmethod
    def __get_matchup(cls, players, is_team=False):
        key = "+" if is_team else "v"
        return key.join(sorted([p.detail_data["race"][0].upper() for p in players]))

    @classmethod
    def __parse_teams(cls, teams, players):
        if len(teams) < len(players):
            # handle teams
            tms = []
            matchup = []
            for team in teams:
                # Parse team info and generate the race makeup
                matchup.append(cls.__get_matchup(team.players, is_team=True))
                tm = [(p.pid, p.name, p.detail_data["race"]) for p in team.players]
                sorted(tm, key=lambda x: x[2][0])
                tms.append(tm)
            return True, tms, "v".join(matchup)
        else:
            return False, None, None

    @classmethod
    def __process_replay(cls, replay_file, load_map=False):
        try:
            engine = sc2reader.engine.GameEngine(plugins=cls.get_plugins())
            replay_bytes = io.BytesIO(replay_file.body)
            # TODO: calculate checksum of replay just in case it is a duplicate
            replay = sc2reader.load_replay(replay_bytes, engine=engine, load_map=load_map, load_level=4)

            is_teams, teams, matchup = cls.__parse_teams(replay.teams, replay.players)

            game = {"stats": defaultdict(lambda: defaultdict(list)), "event": defaultdict(lambda: defaultdict(list))}

            # Handle proper event parsing now
            cache = set([])
            for event in replay.events:
                # Check __event_parsing__ for the right parse function using the type of event. defualt is a no_op
                cls.__event_parsing__.get(type(event), default)(event, game, cls.__give_cache(event, cache))
            # Handle proper map/camera parsing

            data = {
                "analyzed_on": datetime.utcnow().isoformat(),
                "frames": replay.frames,
                "seconds": int(replay.frames / 16),
                "is_ffa": not is_teams and len(replay.players) > 2,
                "is_teams": is_teams,
                "has_ai": len(replay.computers) > 0,
                "matchup": matchup,
                "human_players": [{"pid": h.pid, "name": h.name, "race": h.detail_data['race']} for h in replay.humans],
                "ai_players": [{"pid": c.pid, "name": c.name, "race": c.detail_data['race']} for c in replay.computers],
                "teams": teams,
                "winner": [{"pid": h.pid, "name": h.name, "race": h.detail_data['race']} for h in replay.winner.players],
                "loser": [{"pid": h.pid, "name": h.name, "race": h.detail_data['race']} for h in replay.players if h not in replay.winner.players],

                "ladder": replay.is_ladder,
                "avg_apm": [{"pid": h.pid, "name": h.name, "avg_apm": h.avg_apm} for h in replay.humans],
            }
            if load_map:
                data["map_name"] = replay.map.name
                data["map_url"] = replay.map_file.url

            return data, game
        except:
            traceback.print_exc()
            return None

    @classmethod
    def test_process(cls, replay_file):
        try:
            engine = sc2reader.engine.GameEngine(plugins=cls.get_plugins())
            replay = sc2reader.load_replay(replay_file, engine=engine, load_map=False, load_level=4)

            game = {"stats": defaultdict(lambda: defaultdict(list)), "event": defaultdict(lambda: defaultdict(list))}
            print("Number of events to process", len(replay.events))
            cache = set([])
            for i, event in enumerate(replay.events):
                cls.__event_parsing__.get(type(event), default)(event, game, cls.__give_cache(event, cache))

            print("Done... writing")
            # Write contents to file
            with open("test.json", "w") as test_file:
                test_file.write(json.dumps(game))
        except:
            traceback.print_exc()
            return None

    @classmethod
    def __analyze_replay(cls, replay_file, load_map=False):
        # Simple analysis of the replay file. Will return some basic information
        try:
            engine = sc2reader.engine.GameEngine(plugins=cls.get_plugins())
            # Parse basic information about replay match
            replay = sc2reader.load_replay(io.BytesIO(replay_file.body), engine=engine, load_map=load_map, load_level=2)

            is_teams, teams, matchup = cls.__parse_teams(replay.teams, replay.players)
            if not is_teams:
                # Calculate matchup normally
                teams = []
                matchup = cls.__get_matchup(replay.players)

            basic_info = {
                "analyzed_on": datetime.utcnow().isoformat(),
                "frames": replay.frames,
                "seconds": int(replay.frames / 16),
                "is_ffa": not is_teams and len(replay.players) > 2,
                "is_teams": is_teams,
                "has_ai": len(replay.computers) > 0,
                "matchup": matchup,
                "human_players": [(h.pid, h.name, h.detail_data['race']) for h in replay.humans],
                "ai_players": [(c.pid, c.name, c.detail_data['race']) for c in replay.computers],
                "teams": teams,
                "winner": [(w.pid, w.name, w.detail_data['race']) for w in replay.winner.players],
                "loser": [(p.pid, p.name, p.detail_data['race']) for p in replay.players if p not in replay.winner.players],
                "ladder": replay.is_ladder,
            }
            if load_map:
                basic_info["map_name"] = replay.map.name
                basic_info["map_url"] = replay.map_file.url
            return basic_info
        except:
            traceback.print_exc()
            return None

    @classmethod
    def __extract_events(cls, replay, data):
        for event in replay.events:
            cls.__event_parsing__.get(type(event), default)(event, data)

    @classmethod
    async def analyze_replay(cls, replay_file, load_map=True):
        loop = asyncio.get_event_loop()
        # Todo: I want to return the minimap as well, so, should look into checking for map image in object storage,
        # and returning the URL for it if available, else storing it, and then retrieving
        return await loop.run_in_executor(None, cls.__analyze_replay, replay_file, load_map)

    @classmethod
    async def process_replay(cls, replay_file, load_map=True):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, cls.__process_replay, replay_file, load_map)


if __name__ == "__main__":
    Replay.test_process("/Users/SakuraSound/Developer/IBM/replay_processing/replays/ml_replays/0/030d8420ca7f783e9a1713c66f4eca142ffba96b.SC2Replay")
