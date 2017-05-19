ARMY_UNITS = frozenset(["Marine", "Colossus", "InfestorTerran", "Baneling", "Mothership", "MothershipCore", "Changeling", "SiegeTank", "Viking", "Reaper",
                        "Ghost", "Marauder", "Thor", "Hellion", "Hellbat", "Cyclone", "Liberator", "Medivac", "Banshee", "Raven", "Battlecruiser", "Nuke", "Zealot",
                        "Stalker", "HighTemplar", "Disruptor", "DarkTemplar", "Sentry", "Phoenix", "Carrier", "Oracle", "VoidRay", "Tempest", "WarpPrism", "Observer",
                        "Immortal", "Adept", "Zergling", "Overlord", "Hydralisk", "Mutalisk", "Ultralisk", "Roach", "Infestor", "Corruptor",
                        "BroodLord", "Queen", "Overseer", "Archon", "InfestedTerran", "Ravager", "Viper", "SwarmHost", "SCV", "Drone", "Probe", "WidowMine"])


BASES = frozenset(["CommandCenter", "Nexus", "Hatchery", "Lair", "Hive", "PlanetaryFortress", "OrbitalCommand"])

BUILDINGS = frozenset(["Armory", "Assimilator", "BanelingNest", "Barracks", "Bunker", "CommandCenter", "CyberneticsCore", "DarkShrine", "EngineeringBay",
                       "EvolutionChamber", "Extractor", "Factory", "FleetBeacon", "Forge", "FusionCore", "GhostAcademy", "GreaterSpire", "Hatchery", "Hive",
                       "HydraliskDen", "InfestationPit", "Lair", "LurkerDen", "MissileTurret", "Nexus", "NydusNetwork", "NydusWorm", "OrbitalCommand",
                       "PhotonCannon", "PlanetaryFortress", "Pylon", "Reactor", "Refinery", "RoachWarren", "RoboticsBay", "RoboticsFacility", "SensorTower",
                       "SpawningPool", "SpineCrawler", "Spire", "SporeCrawler", "Starport", "SupplyDepot", "TechLab", "TemplarArchive", "TwilightCouncil", "UltraliskCavern", "WarpGate",
                       "BarracksFlying", "FactoryFlying", "CommandCenterFlying", "OrbitalCommandFlying", "StarportFlying", "BarracksTechLab", "StarportTechLab", "FactoryTechLab",
                       "BarracksReactor", "FactoryReactor", "StarportReactor"])

AIR_UNIT_BUILDINGS = frozenset(["Stargate", "Starport", "Hatchery", "Hive", "Reactor", "RoboticsFacility", "StargateFlying", "StarportReactor"])

AIR_ARMY = frozenset(["Mothership", "MothershipCore", "Viking", "Liberator", "Medivac", "Banshee", "Raven", "Battlecruiser",
                      "Viper", "Mutalisk", "Phoenix", "Oracle", "Carrier", "VoidRay", "Tempest", "Observer", "WarpPrism", "BroodLord",
                      "Corruptor", "Observer", "Overseer"])

AIR_ATTACK = frozenset(["Marine", "InfestedTerran", "Mothership", "Viking", "Ghost", "Thor", "Cyclone", "Liberator", "Raven", "Battlecruiser", "Nuke", "Stalker", "HighTemplar", "Sentry", "Phoenix",
                        "Carrier", "VoidRay", "Tempest", "Hydralisk", "Mutalisk", "Corruptor", "Queen", "Archon", "Infestor", "WidowMine"])

GROUND_ATTACK = frozenset(["Marine", "Colossus", "InfestedTerran", "Baneling", "Mothership", "MothershipCore", "SiegeTank", "Viking", "Reaper", "Ghost", "Marauder", "Thor",
                           "Hellion", "Hellbat", "Cyclone", "Liberator", "Banshee", "Raven", "Battlecruiser", "Nuke", "Zealot", "Stalker", "HighTemplar", "Disruptor", "DarkTemplar",
                           "Sentry", "Carrier", "Oracle", "VoidRay", "Tempest", "Immortal", "Adept", "Zergling", "Hydralisk", "Mutalisk", "Ultralisk", "Roach", "BroodLord", "Queen", "Archon",
                           "Ravager", "Viper", "Infestor", "SwarmHost", "SCV", "Probe", "Drone", "WidowMine"])

AIR_TECH_BUILDINGS = frozenset(["FleetBeacon", "FusionCore", "GreaterSpire", "Spire", "Armory", "CyberneticsCore", "Forge", "Hatchery", "Hive", "Lair", "TechLab", "StarportTechLab"])

ANTI_AIR_BUILDINGS = frozenset(["PhotonCannon", "MissileTurret", "SporeCrawler", "Bunker"])

DEFENSE_BUILDINGS = frozenset(["Bunker", "MissileTurret", "PhotonCannon", "PlanetaryFortress", "SensorTower", "SpineCrawler", "SporeCrawler"])

DETECTORS = frozenset(["PhotonCannon", "SensorTower", "SporeCrawler", "Observer", "Oracle", "Overlord", "Overseer", "MissileTurret", "OrbitalCommand", "Raven"])

GROUND_DEFENSE_BUILDINGS = frozenset(["PhotonCannon", "SpineCrawler", "PlanetaryFortress", "Bunker"])

GROUND_UNIT_BUILDINGS = frozenset(["Barracks", "Factory", "WarpGate", "Hatchery", "Hive", "Reactor", "RoboticsFacility", "BarracksReactor", "FactoryReactor", "BarracksFlying", "FactoryFlying"])

GROUND_ARMY = ARMY_UNITS - AIR_ARMY

GROUND_TECH_BUILDINGS = frozenset(["BanelingNest", "DarkShrine", "EngineeringBay", "EvolutionChamber", "GhostAcademy", "HydraliskDen", "InfestationPit", "LurkerDen",
                                   "RoachWarren", "RoboticsBay", "SpawningPool", "TemplarArchive", "TwilightCouncil", "UltraliskCavern", "Armory", "CyberneticsCore", "Forge", "Hatchery", "Hive", "Lair", "TechLab", "BarracksTechLab", "FactoryTechLab"])


SUPPLY = frozenset(["Overlord", "Overseer", "Pylon", "SupplyDepot"])

TECH_BUILDINGS = frozenset(["Armory", "CyberneticsCore", "Forge", "TechLab", "BanelingNest", "DarkShrine", "EngineeringBay", "EvolutionChamber", "GhostAcademy",
                            "HydraliskDen", "InfestationPit", "LurkerDen", "RoachWarren", "RoboticsBay", "SpawningPool", "TemplarArchive", "TwilightCouncil", "UltraliskCavern",
                            "FleetBeacon", "FusionCore", "GreaterSpire", "Spire", "BarracksTechLab", "FactoryTechLab", "StarportTechLab"])

VESPENE = frozenset(["Assimilator", "Extractor", "Refinery"])

WORKERS = frozenset(["Drone", "Probe", "SCV", "MULE"])

MASSIVE_UNITS = frozenset(["Thor", "Battlecruiser", "Ultralisk", "BroodLord", "Archon", "Colossus", "Carrier", "Mothership", "Tempest"])

LIGHT_UNITS = frozenset(["Probe", "Zealot", "Sentry", "HighTemplar", "DarkTemplar", "Observer", "Phoenix", "Oracle", "Adept", "SCV", "MULE", "Marine", "Reaper", "Hellion", "Raven", "Banshee", "Hellbat",
                         "Drone", "Zergling", "Hydralisk", "Changeling", "InfestedTerran", "Mutalisk", "WidowMine"])

ARMORED_UNITS = frozenset(["Stalker", "Immortal", "Colossus", "WarpPrism", "VoidRay", "Carrier", "Mothership", "Tempest", "MothershipCore", "Disruptor", "Marauder", "SiegeTank", "Thor",
                           "Viking", "Medivac", "Battlecruiser", "Cyclone", "Liberator", "Roach", "Infestor", "Ultralisk", "Overlord", "Overseer", "Corruptor", "BroodLord", "SwarmHost", "Viper", "Lurker"])

BIO_UNITS = frozenset(["Zealot", "HighTemplar", "DarkTemplar", "Adept", "SCV", "Marine", "Marauder", "Reaper", "Ghost", "Hellbat", "Drone", "Queen", "Zergling", "Baneling", "Roach", "Hydralisk", "Infestor", "Ultralisk",
                       "Changeling", "InfestedTerran", "Overlord", "Overseer", "Mutalisk", "Corruptor", "BroodLord", "Viper", "SwarmHost", "Ravager", "Lurker"])

MECH_UNITS = frozenset(["Probe", "Stalker", "Sentry", "Immortal", "Colossus", "Observer", "WarpPrism", "Phoenix", "VoidRay", "Carrier", "Mothership", "MothershipCore", "Oracle", "Tempest", "Disruptor",
                        "SCV", "MULE", "Hellion", "SiegeTank", "Thor", "Viking", "Medivac", "Raven", "Banshee", "Battlecruiser", "Hellbat", "Cyclone", "Liberator", "WidowMine"])

MELEE_UNITS = frozenset(["Probe", "Zealot", "DarkTemplar", "SCV", "Hellbat", "Drone", "Zergling", "Baneling", "Ultralisk"])

RANGED_UNITS = frozenset(["Sentry", "Stalker", "Immortal", "Colossus", "Phoenix", "VoidRay", "Carrier", "Mothership", "Archon", "MothershipCore", "Tempest", "Marine", "Marauder", "Reaper", "Ghost", "Hellion", "SiegeTank",
                          "Thor", "Viking", "Banshee", "Battlecruiser", "Raven", "WidowMine", "Queen", "Roach", "Infestor", "InfestedTerran", "SwarmHost", "BroodLord", "Corruptor", "Mutalisk", "Hydralisk"])

PSIONIC_UNITS = frozenset(["Ghost", "Queen", "Infestor", "Viper", "Sentry", "HighTemplar", "DarkTemplar", "Archon", "WarpPrism", "Mothership", "MothershipCore", "Oracle"])


ABILITIES = frozenset(["250mmStrikeCannons", "AssaultMode", "Corruption", "EMP", "FighterMode", "ForceField", "FungalGrowth", "GravitonBeam", "GuardianShield", "Feedback", "PhaseShield", "Entomb",
                                "PsiStorm", "PsionicStorm", "BuildAutoTurret", "SeekerMissile", "SiegeMode", "Snipe", "Stimpack", "TacNukeStrike", "TacticalNukeStrike", "Transfusion", "Yamato", "YamatoGun"])

AVAILABLE_STRUCTURES = {
    "terran": {
        "SupplyDepot": frozenset(["Barracks"]),
        "CommandCenter": frozenset(["EngineeringBay"]),
        "EngineeringBay": frozenset(["SensorTower", "MissileTurret", "PlanetaryFortress"]),
        "Barracks": frozenset(["OrbitalCommand", "Bunker", "Factory", "GhostAcademy", "Reactor", "TechLab"]),
        "Factory": frozenset(["Armory", "Starport", "Reactor", "TechLab"]),
        "Starport": frozenset(["FusionCore", "Reactor", "TechLab"]),
    },
    "protoss": {
        "Nexus": frozenset(["Forge", "Gateway"]),
        "Forge": frozenset(["PhotonCannon"]),
        "Gateway": frozenset(["CyberneticsCore"]),
        "CyberneticsCore": frozenset(["WarpGate", "TwilightCouncil", "Stargate", "RoboticsFacility"]),
        "TwilightCouncil": frozenset(["TemplarArchive", "DarkShrine"]),
        "Stargate": frozenset(["FleetBeacon"]),
        "RoboticsFacility": frozenset(["RoboticsBay"]),
    },
    "zerg": {
        "Hatchery": frozenset(["SpawningPool", "EvolutionChamber"]),
        "SpawningPool": frozenset(["Lair", "RoachWarren", "BanelingNest", "SpineCrawler", "SporeCrawler"]),
        "Lair": frozenset(["SpawningPool", "EvolutionChamber", "HydraliskDen", "InfestationPit", "Spire", "NydusNetwork"]),
        "InfestationPit": frozenset(["Hive"]),
        "Hive": frozenset(["SpawningPool", "EvolutionChamber", "UltraliskCavern", "GreaterSpire"])
    }
}


AVAILABLE_UPGRADES = {
    "terran": {
        frozenset(["Barracks", "BarracksTechLab"]): frozenset(["ResearchCombatShield", "ResearchStimpack", "ResearchConcussiveShell"]),
        frozenset(["Factory", "FactoryTechLab"]): frozenset(["ResearchSiegeTech", "ResearchInfernalPreIgniter", "Research250mmStrikeCannons", "ResearchTransformationServos", "ResearchDrillingClaws"]),
        frozenset(["Starport", "StarportTechLab"]): frozenset(["ResearchCloakingField", "ResearchCaduceusReactor", "ResearchCorvidReactor", "ResearchSeekerMissile", "ResearchDurableMaterials"]),
        frozenset(["EngineeringBay"]): frozenset(["UpgradeTerranInfantryWeapons1", "UpgradeTerranInfantryArmor1", "ResearchNeosteelFrame", "UpgradeStructureArmor", "ResearchHiSecAutoTracking"]),
        frozenset(["EngineeringBay", "Armory"]): frozenset(["UpgradeTerranInfantryWeapons2", "UpgradeTerranInfantryWeapons3", "UpgradeTerranInfantryArmor2", "UpgradeTerranInfantryArmor3"]),
        frozenset(["Armory"]): frozenset(["UpgradeVehiclePlating1", "UpgradeVehiclePlating2", "UpgradeVehiclePlating3", "UpgradeVehicleWeapons1", "UpgradeVehicleWeapons2", "UpgradeVehicleWeapons3",
                                          "UpgradeShipPlating1", "UpgradeShipPlating2", "UpgradeShipPlating3", "UpgradeShipWeapons1", "UpgradeShipWeapons2", "UpgradeShipWeapons3"]),
        frozenset(["FusionCore"]): frozenset(["ResearchWeaponRefit", "ResearchBehemothReactor"]),
        frozenset(["GhostAcademy"]): frozenset(["ResearchPersonalCloaking", "ResearchMoebiusReactor"]),
    },
    "protoss": {
        frozenset(["Forge"]): frozenset(["UpgradeGroundWeapons1", "UpgradeGroundArmor1", "UpgradeShields1"]),
        frozenset(["Forge", "TwilightCouncil"]): frozenset(["UpgradeGroundWeapons2", "UpgradeGroundWeapons3", "UpgradeGroundArmor2", "UpgradeGroundArmor3", "UpgradeShields2", "UpgradeShields3"]),
        frozenset(["CyberneticsCore"]): frozenset(["UpgradeAirWeapons1", "UpgradeAirArmor1", "ResearchWarpGate"]),
        frozenset(["CyberneticsCore", "FleetBeacon"]): frozenset(["UpgradeAirWeapons2", "UpgradeAirWeapons3", "UpgradeAirArmor2", "UpgradeAirArmor3"]),
        frozenset(["FleetBeacon"]): frozenset(["ResearchFluxVanes", "ResearchGravitonCatapult", "ResearchAnionPulseCrystals", "ResearchBosonicCore", "ResearchGravitySling"]),
        frozenset(["TwilightCouncil"]): frozenset(["ResearchCharge", "ResearchBlink"]),
        frozenset(["RoboticsBay"]): frozenset(["ResearchGraviticBoosters", "ResearchGraviticDrive", "ResearchExtendedThermalLance"]),
        frozenset(["TemplarArchive"]): frozenset(["ResearchKhaydarinAmulet", "ResearchPsiStorm"]),
        frozenset(["DarkShrine"]): frozenset(["ResearchShadowStrike"]),
    },
    "zerg": {
        frozenset(["Hatchery"]): frozenset(["ResearchBurrow", "ResearchPneumatizedCarapace"]),
        frozenset(["Lair"]): frozenset(["ResearchOverlordSpeed", "ResearchVentralSacs", "ResearchBurrow",  "ResearchPneumatizedCarapace"]),
        frozenset(["Hive"]): frozenset(["ResearchOverlordSpeed", "ResearchVentralSacs", "ResearchBurrow",  "ResearchPneumatizedCarapace"]),
        frozenset(["SpawningPool"]): frozenset(["ResearchZerglingAttackSpeed", "ResearchZerglingMovementSpeed"]),
        frozenset(["RoachWarren"]): frozenset(["ResearchRoachSpeed", "ResearchRoachTunnelingClaws"]),
        frozenset(["HydraliskDen", "Lair"]): frozenset(["ResearchHydraliskSpeed"]),
        frozenset(["LurkerDen"]): frozenset(["EvolveGroovedSpines", "EvolveMuscularAugments"]),
        frozenset(["BanelingNest"]): frozenset(["EvolveCentrifugalHooks", "EvolveTunnelingJaws"]),
        frozenset(["Spire"]): frozenset(["EvolveFlyerAttacks1", "EvolveFlyerCarapace1"]),
        frozenset(["Spire", "Hive"]): frozenset(["EvolveFlyerAttacks2", "EvolveFlyerCarapace2"]),
        frozenset(["Spire", "Lair"]): frozenset(["EvolveFlyerAttacks3", "EvolveFlyerCarapace3"]),
        frozenset(["InfestationPit"]): frozenset(["EvolvePathogenGlands", "EvolveNeuralParasite", "EvolveEnduringLocusts"]),
        frozenset(["UltraliskCavern"]): frozenset(["EvolveChitinousPlating", "EvolveBurrowCharge"])
    }

}

AVAILABLE_UNITS = {
    "terran": {
        frozenset(["CommandCenter"]): frozenset(["SCV"]),
        frozenset(["OrbitalCommand"]): frozenset(["MULE"]),
        frozenset(["Barracks"]): frozenset(["Marine", "Reaper"]),
        frozenset(["Barracks", "BarracksTechLab"]): frozenset(["Marauder"]),
        frozenset(["Barracks", "GhostAcademy"]): frozenset(["Ghost"]),
        frozenset(["Factory"]): frozenset(["Hellion", "Cyclone"]),
        frozenset(["Factory", "FactoryTechLab"]): frozenset(["SiegeTank", "Thor"]),
        frozenset(["Factory", "FactoryReactor"]): frozenset(["WidowMine"]),
        frozenset(["Factory", "Armory"]): frozenset(["Hellbat"]),
        frozenset(["Starport"]): frozenset(["Viking", "Medivac", "Liberator"]),
        frozenset(["Starport", "StarportTechLab"]): frozenset(["Banshee", "Raven"]),
        frozenset(["Starport", "StarportTechLab", "FusionCore"]): frozenset(["Battlecruiser"]),
    },
    "protoss": {
        frozenset(["Nexus"]): frozenset(["Probe"]),
        frozenset(["Nexus", "CyberneticsCore"]): frozenset(["MothershipCore"]),
        frozenset(["Nexus", "CyberneticsCore", "FleetBeacon"]): frozenset(["Mothership"]),
        frozenset(["Gateway"]): frozenset(["Zealot", "Adept"]),
        frozenset(["Gateway", "CyberneticsCore"]): frozenset(["Stalker", "Sentry"]),
        frozenset(["Gateway", "TemplarArchive"]): frozenset(["HighTemplar"]),
        frozenset(["Gateway", "DarkShrine"]): frozenset(["DarkTemplar"]),
        frozenset(["WarpGate"]): frozenset(["Zealot", "Adept"]),
        frozenset(["WarpGate", "CyberneticsCore"]): frozenset(["Stalker", "Sentry"]),
        frozenset(["WarpGate", "TemplarArchive"]): frozenset(["HighTemplar"]),
        frozenset(["WarpGate", "DarkShrine"]): frozenset(["DarkTemplar"]),
        frozenset(["RoboticsFacility"]): frozenset(["Observer", "Imomortal", "WarpPrism"]),
        frozenset(["RoboticsFacility", "RoboticsBay"]): frozenset(["Colossus", "Disruptor"]),
        frozenset(["Stargate"]): frozenset(["Phoenix", "Oracle", "VoidRay"]),
        frozenset(["Stargate", "FleetBeacon"]): frozenset(["Carrier", "Tempest"])
    },
    "zerg": {
        frozenset(["Hatchery"]): frozenset(["Drone", "Queen", "Overlord"]),
        frozenset(["Hatchery", "SpawningPool"]): frozenset(["Zergling"]),
        frozenset(["Hatchery", "RoachWarren"]): frozenset(["Roach"]),
        frozenset(["Hatchery", "BanelingNest"]): frozenset(["Baneling"]),
        frozenset(["Hatchery", "HydraliskDen"]): frozenset(["Hydralisk"]),
        frozenset(["Hatchery", "LurkerDen"]): frozenset(["Lurker"]),
        frozenset(["Hatchery", "Spire"]): frozenset(["Mutalisk", "Corruptor"]),
        frozenset(["Hatchery", "GreaterSpire"]): frozenset(["Mutalisk", "Corruptor", "BroodLord"]),
        frozenset(["Hatchery", "InfestationPit"]): frozenset(["Infestor", "SwarmHost"]),
        frozenset(["Hatchery", "UltraliskCavern"]): frozenset(["Ultralisk"]),

        frozenset(["Lair"]): frozenset(["Drone", "Queen", "Overlord"]),
        frozenset(["Lair", "SpawningPool"]): frozenset(["Zergling"]),
        frozenset(["Lair", "RoachWarren"]): frozenset(["Roach"]),
        frozenset(["Lair", "BanelingNest"]): frozenset(["Baneling"]),
        frozenset(["Lair", "HydraliskDen"]): frozenset(["Hydralisk"]),
        frozenset(["Lair", "LurkerDen"]): frozenset(["Lurker"]),
        frozenset(["Lair", "Spire"]): frozenset(["Mutalisk", "Corruptor"]),
        frozenset(["Lair", "GreaterSpire"]): frozenset(["Mutalisk", "Corruptor", "BroodLord"]),
        frozenset(["Lair", "InfestationPit"]): frozenset(["Infestor", "SwarmHost"]),
        frozenset(["Lair", "UltraliskCavern"]): frozenset(["Ultralisk"]),

        frozenset(["Hive"]): frozenset(["Drone", "Queen", "Overlord"]),
        frozenset(["Hive", "SpawningPool"]): frozenset(["Zergling"]),
        frozenset(["Hive", "RoachWarren"]): frozenset(["Roach"]),
        frozenset(["Hive", "BanelingNest"]): frozenset(["Baneling"]),
        frozenset(["Hive", "HydraliskDen"]): frozenset(["Hydralisk"]),
        frozenset(["Hive", "LurkerDen"]): frozenset(["Lurker"]),
        frozenset(["Hive", "Spire"]): frozenset(["Mutalisk", "Corruptor"]),
        frozenset(["Hive", "GreaterSpire"]): frozenset(["Mutalisk", "Corruptor", "BroodLord"]),
        frozenset(["Hive", "InfestationPit"]): frozenset(["Infestor", "SwarmHost"]),
        frozenset(["Hive", "UltraliskCavern"]): frozenset(["Ultralisk"]),
    }




}
