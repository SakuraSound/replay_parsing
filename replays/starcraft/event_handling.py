from replays.starcraft.constants import (BUILDINGS, AIR_ARMY, AIR_ATTACK, AIR_TECH_BUILDINGS,
                                         AIR_UNIT_BUILDINGS, ANTI_AIR_BUILDINGS, ARMORED_UNITS,
                                         ARMY_UNITS, BASES, BIO_UNITS, DEFENSE_BUILDINGS,
                                         DETECTORS, GROUND_ARMY, GROUND_ATTACK,
                                         GROUND_DEFENSE_BUILDINGS, GROUND_UNIT_BUILDINGS,
                                         LIGHT_UNITS, MASSIVE_UNITS, MECH_UNITS, MELEE_UNITS,
                                         PSIONIC_UNITS, RANGED_UNITS, SUPPLY, TECH_BUILDINGS,
                                         VESPENE, WORKERS, ABILITIES)

EVENTS = {
    "worker_events": WORKERS,
    "vespene_events": VESPENE,
    "air_tech_events": AIR_TECH_BUILDINGS,
    "air_structure_events": AIR_UNIT_BUILDINGS,
    "air_army_events": AIR_ARMY,
    "air_attack_events": AIR_ATTACK,
    "air_defense_structure_events": ANTI_AIR_BUILDINGS,
    "army_events": ARMY_UNITS,
    "defense_events": DEFENSE_BUILDINGS,
    "detector_events": DETECTORS,
    "expansion_events": BASES,
    "ground_defense_structure_events": GROUND_DEFENSE_BUILDINGS,
    "ground_structure_events": GROUND_UNIT_BUILDINGS,
    "ground_army_events": GROUND_ARMY,
    "ground_attack_events": GROUND_ATTACK,
    "supply_events": SUPPLY,
    "tech_events": TECH_BUILDINGS,
    "massive_army_events": MASSIVE_UNITS,
    "light_army_events": LIGHT_UNITS,
    "bio_army_events": BIO_UNITS,
    "mech_army_event": MECH_UNITS,
    "armored_army_event": ARMORED_UNITS,
    "melee_army_event": MELEE_UNITS,
    "ranged_army_event": RANGED_UNITS,
    "psionic_army_event": PSIONIC_UNITS,
}

COUNTS = {
    "worker_events": "worker_count",
    "vespene_events": "vespene_structures",
    "air_tech_events": "air_tech_structures",
    "air_unit_events": "air_units_structures",
    "air_defense_structure_events": "air_defense_structures",
    "defense_events": "defense_structures",
    "detector_events": "detectors",
    "expansion_events": "expansion_structures",
    "ground_defense_structure_events": "ground_defense_structures",
    "ground_unit_events": "ground_units_structures",
    "supply_events": "supply_units_structures",
    "tech_events": "tech_structures",
    "army_unit_events": "army_units",
    "air_attack_events": "air_attack_units",
    "ground_attack_events": "ground_attack_units",
    "massive_army_events": "massive_units",
    "light_army_events": "light_units",
    "bio_army_events": "bio_units",
    "mech_army_event": "mech_units",
    "armored_army_event": "armored_units",
    "melee_army_event": "melee_units",
    "ranged_army_event": "ranged_units",
    "psionic_army_event": "psionic_units"
}


def __add_position(data, player, frame, unit_id, unit, x, y):
    if len(data["position"][player][(unit_id, unit)]) == 0:
        data["position"][player][(unit_id, unit)].append((frame, unit, (x, y)))
    else:
        previous = data["position"][player][(unit_id, unit)][-1]
        if previous[2] != (x, y):
            data["position"][player][(unit_id, unit)].append((frame, unit, (x, y)))


def __add_moment(data, player, name, moment):
    data["event"][player][name].append(moment)


def __count(data, player, frame, key, add_value, start=0):
    if len(data["stats"][player][key]) == 0:
        data["stats"][player][key].append((0, start))
    # Get the last value
    last_val = data["stats"][player][key][-1][1]
    data["stats"][player][key].append((frame, last_val + add_value))


def __push_stat(data, player, frame, key, value):
    if len(data["stats"][player][key]) == 0 and frame != 0:
        data["stats"][player][key].append((0, 0))
    data["stats"][player][key].append((frame, value))


def default(event, data, dummy):
    # Effectively a no-op. means we got an event we dont know how to handle...
    pass


def player_stats(event, data, dummy):
    player = str(event.pid)
    frame = event.frame

    mins_per_worker = 0 if event.workers_active_count == 0 else event.minerals_collection_rate / event.workers_active_count
    utilization = 0 if event.food_made == 0 else event.food_used / event.food_made
    worker_ratio = 0 if event.food_used == 0 else event.workers_active_count / event.food_used
    vesp_per_worker = 0 if event.workers_active_count == 0 else event.vespene_collection_rate / event.workers_active_count

    __push_stat(data, player, frame, "workers_active", event.workers_active_count)
    __push_stat(data, player, frame, "mineral_available", event.minerals_current)
    __push_stat(data, player, frame, "mineral_collection_rate", event.minerals_collection_rate)
    __push_stat(data, player, frame, "mineral_cost_active_forces", event.minerals_used_active_forces)
    __push_stat(data, player, frame, "mineral_per_worker_rate", mins_per_worker)
    __push_stat(data, player, frame, "mineral_spend", event.minerals_used_current)
    __push_stat(data, player, frame, "mineral_value_current_technology", event.minerals_used_current_technology)
    __push_stat(data, player, frame, "mineral_value_current_army", event.minerals_used_current_army)
    __push_stat(data, player, frame, "mineral_value_current_economic", event.minerals_used_current_economy)
    __push_stat(data, player, frame, "mineral_cost_active_forces", event.minerals_used_active_forces)

    __push_stat(data, player, frame, "supply_available", int(event.food_made))
    __push_stat(data, player, frame, "supply_consumed", int(event.food_used))
    __push_stat(data, player, frame, "supply_available", int(event.food_made))
    __push_stat(data, player, frame, "supply_utilization", utilization)
    __push_stat(data, player, frame, "worker_supply_ratio", worker_ratio)

    __push_stat(data, player, frame, "vespene_available", event.vespene_current)
    __push_stat(data, player, frame, "vespene_collection_rate", event.vespene_collection_rate)
    __push_stat(data, player, frame, "vespene_per_worker_rate", vesp_per_worker)
    __push_stat(data, player, frame, "vespene_cost_active_forces", event.vespene_used_active_forces)
    __push_stat(data, player, frame, "vespene_spend", event.vespene_used_active_forces)
    __push_stat(data, player, frame, "vespene_cost_active_forces", event.vespene_used_current)
    __push_stat(data, player, frame, "vespene_value_current_technology", event.vespene_used_current_technology)
    __push_stat(data, player, frame, "vespene_value_current_army", event.vespene_used_current_army)
    __push_stat(data, player, frame, "vespene_value_current_economic", event.vespene_used_current_economy)

    __push_stat(data, player, frame, "mineral_destruction", event.minerals_killed)
    __push_stat(data, player, frame, "mineral_destruction_army", event.minerals_killed_army)
    __push_stat(data, player, frame, "mineral_destruction_economic", event.minerals_killed_economy)
    __push_stat(data, player, frame, "mineral_destruction_technology", event.minerals_killed_technology)
    __push_stat(data, player, frame, "mineral_loss", event.minerals_lost)
    __push_stat(data, player, frame, "mineral_loss_army", event.minerals_lost_army)
    __push_stat(data, player, frame, "mineral_loss_economic", event.minerals_lost_economy)
    __push_stat(data, player, frame, "mineral_loss_technology", event.minerals_lost_technology)

    __push_stat(data, player, frame, "vespene_destruction", event.vespene_killed)
    __push_stat(data, player, frame, "vespene_destruction_army", event.vespene_killed_army)
    __push_stat(data, player, frame, "vespene_destruction_economic", event.vespene_killed_economy)
    __push_stat(data, player, frame, "vespene_destruction_technology", event.vespene_killed_technology)
    __push_stat(data, player, frame, "vespene_loss", event.vespene_lost)
    __push_stat(data, player, frame, "vespene_loss_army", event.vespene_lost_army)
    __push_stat(data, player, frame, "vespene_loss_economic", event.vespene_lost_economy)
    __push_stat(data, player, frame, "vespene_loss_technology", event.vespene_lost_technology)


def get_original_unit_type(event):
    t = event.unit.type_history[list(event.unit.type_history.keys())[0]]
    return t.name


def unit_born(event, data, cache):
    # Handles all aspects of this event
    unit = event.unit_type_name
    unit_id = event.unit.id
    player = str(event.control_pid)
    frame = event.frame
    moment = {"frame": frame, "event": "create", "unit_id": unit_id, "unit": unit}
    # Keep track of count of unit/buildings active
    if unit in BUILDINGS or unit in ARMY_UNITS:
        __count(data, player, frame, unit + "_count", 1)
        cache.discard(unit_id)
    for name, eligible in EVENTS.items():
        if unit in eligible:
            __add_moment(data, player, name, moment)
            if name in COUNTS:
                __count(data, player, frame, COUNTS[name], 1)


def unit_done(event, data, cache):
    unit = get_original_unit_type(event)
    unit_id = event.unit.id
    frame = event.frame
    moment = {"frame": frame, "event": "create", "unit_id": unit_id, "unit": unit}
    player = str(event.unit.owner.pid)
    if unit in BUILDINGS or unit in ARMY_UNITS:
        __count(data, player, frame, unit + "_count", 1, start=1 if unit in BASES else 0)
    for name, eligible in EVENTS.items():
        if unit in eligible:
            __add_moment(data, player, name, moment)
            cache.discard(unit_id)
            # TODO: update the tech tree and possible units that can be created
            if name in COUNTS:
                start_val = 1 if COUNTS[name] == "expansion_structure" else 0
                __count(data, player, frame, COUNTS[name], 1, start=start_val)
                if unit in BUILDINGS and event.unit.owner.detail_data['race'] == 'Zerg':
                    # Need to subtract one drone for the building
                    __count(data, player, frame, "Drone_count", -1)


def handle_change_timeline(event, frame):
    timeline = [i for i in event.unit.type_history.keys() if i <= event.frame]
    ct_frame = timeline[len(timeline) - 1]
    change_to = event.unit.type_history[ct_frame].name
    cf_frame = timeline[len(timeline) - 2]
    change_from = event.unit.type_history[cf_frame].name
    return change_from, change_to


def unit_type_change(event, data, dummy):
    unit = event.unit.name
    unit_id = event.unit.id
    frame = event.frame
    for name, eligible in EVENTS.items():
        if unit in eligible:
            player = str(event.unit.owner.pid)

            change_from, change_to = handle_change_timeline(event, frame)
            moment = {"frame": frame, "event": "change", "unit_id": unit_id, "change_to": change_to, "change_from": change_from}
            __add_moment(data, player, name, moment)
            if name in COUNTS:
                if COUNTS[name] in ["ground_units_structures", "expansion_structures", "tech_structures", "air_units_structures"]:
                    __count(data, player, frame, change_from + "_count", -1, start=0)
                    __count(data, player, frame, change_to + "_count", 1, start=0)


def upgrade_complete(event, data, dummy):
    if event.frame > 0 and not event.upgrade_type_name.startswith("Spray"):
        player = str(event.pid)
        frame = event.frame
        moment = {"frame": frame, "event": "upgrade", "upgrade": event.upgrade_type_name}
        __add_moment(data, player, "upgrades", moment)


def unit_died(event, data, cache):
    unit = event.unit.name
    unit_id = event.unit.id
    frame = event.frame
    if unit_id not in cache:
        # If its not in unit_cache, then it was successfully created (wasnt destroyed by user, opponent, etc. before complete event)
        for name, eligible in EVENTS.items():
            if unit in eligible:
                pid = str(event.unit.owner.pid)
                moment = {"frame": frame, "event": "die", "unit_id": unit_id, "unit": unit, "x": event.x, "y": event.y}
                __add_moment(data, pid, name, moment)
                if name in COUNTS:
                    start_val = 1 if COUNTS[name] == "expansion_structure" else 0
                    __count(data, pid, frame, COUNTS[name], -1, start=start_val)


def target_ability(event, data, dummy):
    frame = event.frame
    player = str(event.pid)
    if event.ability_name in ABILITIES:
        moment = {"frame": frame, "event": "ability_targeted", "ability": event.ability_name, "x": event.x, "y": event.y}
        __add_moment(data, player, "ability_casted", moment)
        __count(data, player, frame, event.ability_name + "_command_count", 1)


def unit_init(event, data, cache):
    cache.add(event.unit.id)

# Will try to get this working later...
# def unit_position(event, data):
#   frame = event.frame
#    import pdb; pdb.set_trace()
#    print("unit_position_update")
#    print(event.items)
#    print(event.units)
