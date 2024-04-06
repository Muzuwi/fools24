TILESET_JOHTO="TilesetJohto"
TILESET_JOHTO_MODERN="TilesetJohtoModern"
TILESET_KANTO="TilesetKanto"
TILESET_BATTLE_TOWER_OUTSIDE="TilesetBattleTowerOutside"
TILESET_HOUSE="TilesetHouse"
TILESET_PLAYERS_HOUSE="TilesetPlayersHouse"
TILESET_POKECENTER="TilesetPokecenter"
TILESET_GATE="TilesetGate"
TILESET_PORT="TilesetPort"
TILESET_LAB="TilesetLab"
TILESET_FACILITY="TilesetFacility"
TILESET_MART="TilesetMart"
TILESET_MANSION="TilesetMansion"
TILESET_GAME_CORNER="TilesetGameCorner"
TILESET_ELITE_FOUR_ROOM="TilesetEliteFourRoom"
TILESET_TRADITIONAL_HOUSE="TilesetTraditionalHouse"
TILESET_TRAIN_STATION="TilesetTrainStation"
TILESET_CHAMPIONS_ROOM="TilesetChampionsRoom"
TILESET_LIGHTHOUSE="TilesetLighthouse"
TILESET_PLAYERS_ROOM="TilesetPlayersRoom"
TILESET_POKECOM_CENTER="TilesetPokeComCenter"
TILESET_BATTLE_TOWER_INSIDE="TilesetBattleTowerInside"
TILESET_TOWER="TilesetTower"
TILESET_CAVE="TilesetCave"
TILESET_PARK="TilesetPark"
TILESET_RUINS_OF_ALPH="TilesetRuinsOfAlph"
TILESET_RADIO_TOWER="TilesetRadioTower"
TILESET_UNDERGROUND="TilesetUnderground"
TILESET_ICE_PATH="TilesetIcePath"
TILESET_DARK_CAVE="TilesetDarkCave"
TILESET_FOREST="TilesetForest"
TILESET_BETA_WORD_ROOM="TilesetBetaWordRoom"
TILESET_HO_OH_WORD_ROOM="TilesetHoOhWordRoom"
TILESET_KABUTO_WORD_ROOM="TilesetKabutoWordRoom"
TILESET_OMANYTE_WORD_ROOM="TilesetOmanyteWordRoom"
TILESET_AERODACTYL_WORD_ROOM="TilesetAerodactylWordRoom"

# This abomination was generated by running `grep "map " maps.asm` and manually
# processing the output.
MAP_TO_TILESET_DATA = {
    "OlivinePokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "OlivineGym": {
        "tileset": TILESET_CHAMPIONS_ROOM,
        "type": "INDOOR",
    },
    "OlivineTimsHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "OlivineHouseBeta": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "OlivinePunishmentSpeechHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "OlivineGoodRodHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "OlivineCafe": {
        "tileset": TILESET_GAME_CORNER,
        "type": "INDOOR",
    },
    "OlivineMart": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "Route38EcruteakGate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "Route39Barn": {
        "tileset": TILESET_TRADITIONAL_HOUSE,
        "type": "INDOOR",
    },
    "Route39Farmhouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "Route38": {
        "tileset": TILESET_JOHTO,
        "type": "ROUTE",
    },
    "Route39": {
        "tileset": TILESET_JOHTO,
        "type": "ROUTE",
    },
    "OlivineCity": {
        "tileset": TILESET_JOHTO,
        "type": "TOWN",
    },
    "MahoganyRedGyaradosSpeechHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "MahoganyGym": {
        "tileset": TILESET_ELITE_FOUR_ROOM,
        "type": "INDOOR",
    },
    "MahoganyPokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "Route42EcruteakGate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "Route42": {
        "tileset": TILESET_JOHTO,
        "type": "ROUTE",
    },
    "Route44": {
        "tileset": TILESET_JOHTO,
        "type": "ROUTE",
    },
    "MahoganyTown": {
        "tileset": TILESET_JOHTO,
        "type": "TOWN",
    },
    "SproutTower1F": {
        "tileset": TILESET_TOWER,
        "type": "DUNGEON",
    },
    "SproutTower2F": {
        "tileset": TILESET_TOWER,
        "type": "DUNGEON",
    },
    "SproutTower3F": {
        "tileset": TILESET_TOWER,
        "type": "DUNGEON",
    },
    "TinTower1F": {
        "tileset": TILESET_TOWER,
        "type": "DUNGEON",
    },
    "TinTower2F": {
        "tileset": TILESET_TOWER,
        "type": "DUNGEON",
    },
    "TinTower3F": {
        "tileset": TILESET_TOWER,
        "type": "DUNGEON",
    },
    "TinTower4F": {
        "tileset": TILESET_TOWER,
        "type": "DUNGEON",
    },
    "TinTower5F": {
        "tileset": TILESET_TOWER,
        "type": "DUNGEON",
    },
    "TinTower6F": {
        "tileset": TILESET_TOWER,
        "type": "DUNGEON",
    },
    "TinTower7F": {
        "tileset": TILESET_TOWER,
        "type": "DUNGEON",
    },
    "TinTower8F": {
        "tileset": TILESET_TOWER,
        "type": "DUNGEON",
    },
    "TinTower9F": {
        "tileset": TILESET_TOWER,
        "type": "DUNGEON",
    },
    "BurnedTower1F": {
        "tileset": TILESET_TOWER,
        "type": "DUNGEON",
    },
    "BurnedTowerB1F": {
        "tileset": TILESET_CAVE,
        "type": "CAVE",
    },
    "NationalPark": {
        "tileset": TILESET_PARK,
        "type": "ROUTE",
    },
    "NationalParkBugContest": {
        "tileset": TILESET_PARK,
        "type": "ROUTE",
    },
    "RadioTower1F": {
        "tileset": TILESET_RADIO_TOWER,
        "type": "INDOOR",
    },
    "RadioTower2F": {
        "tileset": TILESET_RADIO_TOWER,
        "type": "INDOOR",
    },
    "RadioTower3F": {
        "tileset": TILESET_RADIO_TOWER,
        "type": "INDOOR",
    },
    "RadioTower4F": {
        "tileset": TILESET_RADIO_TOWER,
        "type": "INDOOR",
    },
    "RadioTower5F": {
        "tileset": TILESET_RADIO_TOWER,
        "type": "INDOOR",
    },
    "RuinsOfAlphOutside": {
        "tileset": TILESET_JOHTO,
        "type": "ROUTE",
    },
    "RuinsOfAlphHoOhChamber": {
        "tileset": TILESET_RUINS_OF_ALPH,
        "type": "DUNGEON",
    },
    "RuinsOfAlphKabutoChamber": {
        "tileset": TILESET_RUINS_OF_ALPH,
        "type": "DUNGEON",
    },
    "RuinsOfAlphOmanyteChamber": {
        "tileset": TILESET_RUINS_OF_ALPH,
        "type": "DUNGEON",
    },
    "RuinsOfAlphAerodactylChamber": {
        "tileset": TILESET_RUINS_OF_ALPH,
        "type": "DUNGEON",
    },
    "RuinsOfAlphInnerChamber": {
        "tileset": TILESET_RUINS_OF_ALPH,
        "type": "DUNGEON",
    },
    "RuinsOfAlphResearchCenter": {
        "tileset": TILESET_FACILITY,
        "type": "INDOOR",
    },
    "RuinsOfAlphHoOhItemRoom": {
        "tileset": TILESET_RUINS_OF_ALPH,
        "type": "DUNGEON",
    },
    "RuinsOfAlphKabutoItemRoom": {
        "tileset": TILESET_RUINS_OF_ALPH,
        "type": "DUNGEON",
    },
    "RuinsOfAlphOmanyteItemRoom": {
        "tileset": TILESET_RUINS_OF_ALPH,
        "type": "DUNGEON",
    },
    "RuinsOfAlphAerodactylItemRoom": {
        "tileset": TILESET_RUINS_OF_ALPH,
        "type": "DUNGEON",
    },
    "RuinsOfAlphHoOhWordRoom": {
        "tileset": TILESET_HO_OH_WORD_ROOM,
        "type": "DUNGEON",
    },
    "RuinsOfAlphKabutoWordRoom": {
        "tileset": TILESET_KABUTO_WORD_ROOM,
        "type": "DUNGEON",
    },
    "RuinsOfAlphOmanyteWordRoom": {
        "tileset": TILESET_OMANYTE_WORD_ROOM,
        "type": "DUNGEON",
    },
    "RuinsOfAlphAerodactylWordRoom": {
        "tileset": TILESET_AERODACTYL_WORD_ROOM,
        "type": "DUNGEON",
    },
    "UnionCave1F": {
        "tileset": TILESET_CAVE,
        "type": "CAVE",
    },
    "UnionCaveB1F": {
        "tileset": TILESET_CAVE,
        "type": "CAVE",
    },
    "UnionCaveB2F": {
        "tileset": TILESET_CAVE,
        "type": "CAVE",
    },
    "SlowpokeWellB1F": {
        "tileset": TILESET_CAVE,
        "type": "CAVE",
    },
    "SlowpokeWellB2F": {
        "tileset": TILESET_CAVE,
        "type": "CAVE",
    },
    "OlivineLighthouse1F": {
        "tileset": TILESET_LIGHTHOUSE,
        "type": "DUNGEON",
    },
    "OlivineLighthouse2F": {
        "tileset": TILESET_LIGHTHOUSE,
        "type": "DUNGEON",
    },
    "OlivineLighthouse3F": {
        "tileset": TILESET_LIGHTHOUSE,
        "type": "DUNGEON",
    },
    "OlivineLighthouse4F": {
        "tileset": TILESET_LIGHTHOUSE,
        "type": "DUNGEON",
    },
    "OlivineLighthouse5F": {
        "tileset": TILESET_LIGHTHOUSE,
        "type": "DUNGEON",
    },
    "OlivineLighthouse6F": {
        "tileset": TILESET_LIGHTHOUSE,
        "type": "DUNGEON",
    },
    "MahoganyMart1F": {
        "tileset": TILESET_TRADITIONAL_HOUSE,
        "type": "INDOOR",
    },
    "TeamRocketBaseB1F": {
        "tileset": TILESET_UNDERGROUND,
        "type": "DUNGEON",
    },
    "TeamRocketBaseB2F": {
        "tileset": TILESET_FACILITY,
        "type": "DUNGEON",
    },
    "TeamRocketBaseB3F": {
        "tileset": TILESET_FACILITY,
        "type": "DUNGEON",
    },
    "IlexForest": {
        "tileset": TILESET_FOREST,
        "type": "CAVE",
    },
    "GoldenrodUnderground": {
        "tileset": TILESET_GATE,
        "type": "DUNGEON",
    },
    "GoldenrodUndergroundSwitchRoomEntrances": {
        "tileset": TILESET_ELITE_FOUR_ROOM,
        "type": "DUNGEON",
    },
    "GoldenrodDeptStoreB1F": {
        "tileset": TILESET_UNDERGROUND,
        "type": "DUNGEON",
    },
    "GoldenrodUndergroundWarehouse": {
        "tileset": TILESET_UNDERGROUND,
        "type": "DUNGEON",
    },
    "MountMortar1FOutside": {
        "tileset": TILESET_DARK_CAVE,
        "type": "CAVE",
    },
    "MountMortar1FInside": {
        "tileset": TILESET_DARK_CAVE,
        "type": "CAVE",
    },
    "MountMortar2FInside": {
        "tileset": TILESET_DARK_CAVE,
        "type": "CAVE",
    },
    "MountMortarB1F": {
        "tileset": TILESET_DARK_CAVE,
        "type": "CAVE",
    },
    "IcePath1F": {
        "tileset": TILESET_ICE_PATH,
        "type": "CAVE",
    },
    "IcePathB1F": {
        "tileset": TILESET_ICE_PATH,
        "type": "CAVE",
    },
    "IcePathB2FMahoganySide": {
        "tileset": TILESET_ICE_PATH,
        "type": "CAVE",
    },
    "IcePathB2FBlackthornSide": {
        "tileset": TILESET_ICE_PATH,
        "type": "CAVE",
    },
    "IcePathB3F": {
        "tileset": TILESET_ICE_PATH,
        "type": "CAVE",
    },
    "WhirlIslandNW": {
        "tileset": TILESET_DARK_CAVE,
        "type": "CAVE",
    },
    "WhirlIslandNE": {
        "tileset": TILESET_DARK_CAVE,
        "type": "CAVE",
    },
    "WhirlIslandSW": {
        "tileset": TILESET_DARK_CAVE,
        "type": "CAVE",
    },
    "WhirlIslandCave": {
        "tileset": TILESET_DARK_CAVE,
        "type": "CAVE",
    },
    "WhirlIslandSE": {
        "tileset": TILESET_DARK_CAVE,
        "type": "CAVE",
    },
    "WhirlIslandB1F": {
        "tileset": TILESET_DARK_CAVE,
        "type": "CAVE",
    },
    "WhirlIslandB2F": {
        "tileset": TILESET_DARK_CAVE,
        "type": "CAVE",
    },
    "WhirlIslandLugiaChamber": {
        "tileset": TILESET_DARK_CAVE,
        "type": "CAVE",
    },
    "SilverCaveRoom1": {
        "tileset": TILESET_DARK_CAVE,
        "type": "CAVE",
    },
    "SilverCaveRoom2": {
        "tileset": TILESET_CAVE,
        "type": "CAVE",
    },
    "SilverCaveRoom3": {
        "tileset": TILESET_CAVE,
        "type": "CAVE",
    },
    "SilverCaveItemRooms": {
        "tileset": TILESET_CAVE,
        "type": "CAVE",
    },
    "DarkCaveVioletEntrance": {
        "tileset": TILESET_DARK_CAVE,
        "type": "CAVE",
    },
    "DarkCaveBlackthornEntrance": {
        "tileset": TILESET_DARK_CAVE,
        "type": "CAVE",
    },
    "DragonsDen1F": {
        "tileset": TILESET_CAVE,
        "type": "CAVE",
    },
    "DragonsDenB1F": {
        "tileset": TILESET_JOHTO,
        "type": "CAVE",
    },
    "DragonShrine": {
        "tileset": TILESET_LAB,
        "type": "INDOOR",
    },
    "TohjoFalls": {
        "tileset": TILESET_CAVE,
        "type": "CAVE",
    },
    "DiglettsCave": {
        "tileset": TILESET_CAVE,
        "type": "CAVE",
    },
    "MountMoon": {
        "tileset": TILESET_CAVE,
        "type": "CAVE",
    },
    "UndergroundPath": {
        "tileset": TILESET_UNDERGROUND,
        "type": "GATE",
    },
    "RockTunnel1F": {
        "tileset": TILESET_DARK_CAVE,
        "type": "CAVE",
    },
    "RockTunnelB1F": {
        "tileset": TILESET_DARK_CAVE,
        "type": "CAVE",
    },
    "SafariZoneFuchsiaGateBeta": {
        "tileset": TILESET_GATE,
        "type": "INDOOR",
    },
    "SafariZoneBeta": {
        "tileset": TILESET_PARK,
        "type": "CAVE",
    },
    "VictoryRoad": {
        "tileset": TILESET_CAVE,
        "type": "CAVE",
    },
    "EcruteakTinTowerEntrance": {
        "tileset": TILESET_TOWER,
        "type": "INDOOR",
    },
    "WiseTriosRoom": {
        "tileset": TILESET_TRADITIONAL_HOUSE,
        "type": "INDOOR",
    },
    "EcruteakPokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "EcruteakLugiaSpeechHouse": {
        "tileset": TILESET_TRADITIONAL_HOUSE,
        "type": "INDOOR",
    },
    "DanceTheater": {
        "tileset": TILESET_TRADITIONAL_HOUSE,
        "type": "INDOOR",
    },
    "EcruteakMart": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "EcruteakGym": {
        "tileset": TILESET_TOWER,
        "type": "INDOOR",
    },
    "EcruteakItemfinderHouse": {
        "tileset": TILESET_TRADITIONAL_HOUSE,
        "type": "INDOOR",
    },
    "EcruteakCity": {
        "tileset": TILESET_JOHTO,
        "type": "TOWN",
    },
    "BlackthornGym1F": {
        "tileset": TILESET_ELITE_FOUR_ROOM,
        "type": "INDOOR",
    },
    "BlackthornGym2F": {
        "tileset": TILESET_ELITE_FOUR_ROOM,
        "type": "INDOOR",
    },
    "BlackthornDragonSpeechHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "BlackthornEmysHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "BlackthornMart": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "BlackthornPokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "MoveDeletersHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "Route45": {
        "tileset": TILESET_JOHTO,
        "type": "ROUTE",
    },
    "Route46": {
        "tileset": TILESET_JOHTO,
        "type": "ROUTE",
    },
    "BlackthornCity": {
        "tileset": TILESET_JOHTO,
        "type": "TOWN",
    },
    "CinnabarPokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "CinnabarPokecenter2FBeta": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "Route19FuchsiaGate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "SeafoamGym": {
        "tileset": TILESET_CAVE,
        "type": "INDOOR",
    },
    "Route19": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "Route20": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "Route21": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "CinnabarIsland": {
        "tileset": TILESET_KANTO,
        "type": "TOWN",
    },
    "CeruleanGymBadgeSpeechHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "CeruleanPoliceStation": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "CeruleanTradeSpeechHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "CeruleanPokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "CeruleanPokecenter2FBeta": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "CeruleanGym": {
        "tileset": TILESET_PORT,
        "type": "INDOOR",
    },
    "CeruleanMart": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "Route10Pokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "Route10Pokecenter2FBeta": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "PowerPlant": {
        "tileset": TILESET_FACILITY,
        "type": "INDOOR",
    },
    "BillsHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "Route4": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "Route9": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "Route10North": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "Route24": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "Route25": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "CeruleanCity": {
        "tileset": TILESET_KANTO,
        "type": "TOWN",
    },
    "AzaleaPokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "CharcoalKiln": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "AzaleaMart": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "KurtsHouse": {
        "tileset": TILESET_TRADITIONAL_HOUSE,
        "type": "INDOOR",
    },
    "AzaleaGym": {
        "tileset": TILESET_ELITE_FOUR_ROOM,
        "type": "INDOOR",
    },
    "Route33": {
        "tileset": TILESET_JOHTO_MODERN,
        "type": "ROUTE",
    },
    "AzaleaTown": {
        "tileset": TILESET_JOHTO_MODERN,
        "type": "TOWN",
    },
    "LakeOfRageHiddenPowerHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "LakeOfRageMagikarpHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "Route43MahoganyGate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "Route43Gate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "Route43": {
        "tileset": TILESET_JOHTO,
        "type": "ROUTE",
    },
    "LakeOfRage": {
        "tileset": TILESET_JOHTO,
        "type": "TOWN",
    },
    "Route32": {
        "tileset": TILESET_JOHTO,
        "type": "ROUTE",
    },
    "Route35": {
        "tileset": TILESET_JOHTO,
        "type": "ROUTE",
    },
    "Route36": {
        "tileset": TILESET_JOHTO,
        "type": "ROUTE",
    },
    "Route37": {
        "tileset": TILESET_JOHTO,
        "type": "ROUTE",
    },
    "VioletCity": {
        "tileset": TILESET_JOHTO,
        "type": "TOWN",
    },
    "VioletMart": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "VioletGym": {
        "tileset": TILESET_ELITE_FOUR_ROOM,
        "type": "INDOOR",
    },
    "EarlsPokemonAcademy": {
        "tileset": TILESET_LAB,
        "type": "INDOOR",
    },
    "VioletNicknameSpeechHouse": {
        "tileset": TILESET_TRADITIONAL_HOUSE,
        "type": "INDOOR",
    },
    "VioletPokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "VioletKylesHouse": {
        "tileset": TILESET_TRADITIONAL_HOUSE,
        "type": "INDOOR",
    },
    "Route32RuinsOfAlphGate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "Route32Pokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "Route35GoldenrodGate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "Route35NationalParkGate": {
        "tileset": TILESET_GATE,
        "type": "INDOOR",
    },
    "Route36RuinsOfAlphGate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "Route36NationalParkGate": {
        "tileset": TILESET_GATE,
        "type": "INDOOR",
    },
    "Route34": {
        "tileset": TILESET_JOHTO_MODERN,
        "type": "ROUTE",
    },
    "GoldenrodCity": {
        "tileset": TILESET_JOHTO_MODERN,
        "type": "TOWN",
    },
    "GoldenrodGym": {
        "tileset": TILESET_ELITE_FOUR_ROOM,
        "type": "INDOOR",
    },
    "GoldenrodBikeShop": {
        "tileset": TILESET_CHAMPIONS_ROOM,
        "type": "INDOOR",
    },
    "GoldenrodHappinessRater": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "BillsFamilysHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "GoldenrodMagnetTrainStation": {
        "tileset": TILESET_TRAIN_STATION,
        "type": "INDOOR",
    },
    "GoldenrodFlowerShop": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "GoldenrodPPSpeechHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "GoldenrodNameRater": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "GoldenrodDeptStore1F": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "GoldenrodDeptStore2F": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "GoldenrodDeptStore3F": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "GoldenrodDeptStore4F": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "GoldenrodDeptStore5F": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "GoldenrodDeptStore6F": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "GoldenrodDeptStoreElevator": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "GoldenrodDeptStoreRoof": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "GoldenrodGameCorner": {
        "tileset": TILESET_GAME_CORNER,
        "type": "INDOOR",
    },
    "GoldenrodPokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "PokecomCenterAdminOfficeMobile": {
        "tileset": TILESET_POKECOM_CENTER,
        "type": "INDOOR",
    },
    "IlexForestAzaleaGate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "Route34IlexForestGate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "DayCare": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "Route6": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "Route11": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "VermilionCity": {
        "tileset": TILESET_KANTO,
        "type": "TOWN",
    },
    "VermilionFishingSpeechHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "VermilionPokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "VermilionPokecenter2FBeta": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "PokemonFanClub": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "VermilionMagnetTrainSpeechHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "VermilionMart": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "VermilionDiglettsCaveSpeechHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "VermilionGym": {
        "tileset": TILESET_GAME_CORNER,
        "type": "INDOOR",
    },
    "Route6SaffronGate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "Route6UndergroundPathEntrance": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "Route1": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "PalletTown": {
        "tileset": TILESET_KANTO,
        "type": "TOWN",
    },
    "RedsHouse1F": {
        "tileset": TILESET_PLAYERS_HOUSE,
        "type": "INDOOR",
    },
    "RedsHouse2F": {
        "tileset": TILESET_PLAYERS_HOUSE,
        "type": "INDOOR",
    },
    "BluesHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "OaksLab": {
        "tileset": TILESET_LAB,
        "type": "INDOOR",
    },
    "Route3": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "PewterCity": {
        "tileset": TILESET_KANTO,
        "type": "TOWN",
    },
    "PewterNidoranSpeechHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "PewterGym": {
        "tileset": TILESET_TOWER,
        "type": "INDOOR",
    },
    "PewterMart": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "PewterPokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "PewterPokecenter2FBeta": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "PewterSnoozeSpeechHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "OlivinePort": {
        "tileset": TILESET_PORT,
        "type": "ROUTE",
    },
    "VermilionPort": {
        "tileset": TILESET_PORT,
        "type": "ROUTE",
    },
    "FastShip1F": {
        "tileset": TILESET_LIGHTHOUSE,
        "type": "INDOOR",
    },
    "FastShipCabins_NNW_NNE_NE": {
        "tileset": TILESET_LIGHTHOUSE,
        "type": "INDOOR",
    },
    "FastShipCabins_SW_SSW_NW": {
        "tileset": TILESET_LIGHTHOUSE,
        "type": "INDOOR",
    },
    "FastShipCabins_SE_SSE_CaptainsCabin": {
        "tileset": TILESET_LIGHTHOUSE,
        "type": "INDOOR",
    },
    "FastShipB1F": {
        "tileset": TILESET_LIGHTHOUSE,
        "type": "INDOOR",
    },
    "OlivinePortPassage": {
        "tileset": TILESET_UNDERGROUND,
        "type": "INDOOR",
    },
    "VermilionPortPassage": {
        "tileset": TILESET_UNDERGROUND,
        "type": "INDOOR",
    },
    "MountMoonSquare": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "MountMoonGiftShop": {
        "tileset": TILESET_TRADITIONAL_HOUSE,
        "type": "INDOOR",
    },
    "TinTowerRoof": {
        "tileset": TILESET_TOWER,
        "type": "ROUTE",
    },
    "Route23": {
        "tileset": TILESET_KANTO,
        "type": "TOWN",
    },
    "IndigoPlateauPokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "WillsRoom": {
        "tileset": TILESET_ELITE_FOUR_ROOM,
        "type": "INDOOR",
    },
    "KogasRoom": {
        "tileset": TILESET_ELITE_FOUR_ROOM,
        "type": "INDOOR",
    },
    "BrunosRoom": {
        "tileset": TILESET_ELITE_FOUR_ROOM,
        "type": "INDOOR",
    },
    "KarensRoom": {
        "tileset": TILESET_ELITE_FOUR_ROOM,
        "type": "INDOOR",
    },
    "LancesRoom": {
        "tileset": TILESET_CHAMPIONS_ROOM,
        "type": "INDOOR",
    },
    "HallOfFame": {
        "tileset": TILESET_ICE_PATH,
        "type": "INDOOR",
    },
    "Route13": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "Route14": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "Route15": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "Route18": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "FuchsiaCity": {
        "tileset": TILESET_KANTO,
        "type": "TOWN",
    },
    "FuchsiaMart": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "SafariZoneMainOffice": {
        "tileset": TILESET_GAME_CORNER,
        "type": "INDOOR",
    },
    "FuchsiaGym": {
        "tileset": TILESET_LAB,
        "type": "INDOOR",
    },
    "BillsBrothersHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "FuchsiaPokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "FuchsiaPokecenter2FBeta": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "SafariZoneWardensHome": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "Route15FuchsiaGate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "Route8": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "Route12": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "Route10South": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "LavenderTown": {
        "tileset": TILESET_KANTO,
        "type": "TOWN",
    },
    "LavenderPokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "LavenderPokecenter2FBeta": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "MrFujisHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "LavenderSpeechHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "LavenderNameRater": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "LavenderMart": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "SoulHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "LavRadioTower1F": {
        "tileset": TILESET_RADIO_TOWER,
        "type": "INDOOR",
    },
    "Route8SaffronGate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "Route12SuperRodHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "Route28": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "SilverCaveOutside": {
        "tileset": TILESET_KANTO,
        "type": "TOWN",
    },
    "SilverCavePokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "Route28SteelWingHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "Pokecenter2F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "TradeCenter": {
        "tileset": TILESET_GATE,
        "type": "INDOOR",
    },
    "Colosseum": {
        "tileset": TILESET_GATE,
        "type": "INDOOR",
    },
    "TimeCapsule": {
        "tileset": TILESET_GATE,
        "type": "INDOOR",
    },
    "MobileTradeRoom": {
        "tileset": TILESET_MANSION,
        "type": "INDOOR",
    },
    "MobileBattleRoom": {
        "tileset": TILESET_MANSION,
        "type": "INDOOR",
    },
    "Route7": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "Route16": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "Route17": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "CeladonCity": {
        "tileset": TILESET_KANTO,
        "type": "TOWN",
    },
    "CeladonDeptStore1F": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "CeladonDeptStore2F": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "CeladonDeptStore3F": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "CeladonDeptStore4F": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "CeladonDeptStore5F": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "CeladonDeptStore6F": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "CeladonDeptStoreElevator": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "CeladonMansion1F": {
        "tileset": TILESET_MANSION,
        "type": "INDOOR",
    },
    "CeladonMansion2F": {
        "tileset": TILESET_MANSION,
        "type": "INDOOR",
    },
    "CeladonMansion3F": {
        "tileset": TILESET_MANSION,
        "type": "INDOOR",
    },
    "CeladonMansionRoof": {
        "tileset": TILESET_MANSION,
        "type": "INDOOR",
    },
    "CeladonMansionRoofHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "CeladonPokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "CeladonPokecenter2FBeta": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "CeladonGameCorner": {
        "tileset": TILESET_GAME_CORNER,
        "type": "INDOOR",
    },
    "CeladonGameCornerPrizeRoom": {
        "tileset": TILESET_GAME_CORNER,
        "type": "INDOOR",
    },
    "CeladonGym": {
        "tileset": TILESET_TRAIN_STATION,
        "type": "INDOOR",
    },
    "CeladonCafe": {
        "tileset": TILESET_GAME_CORNER,
        "type": "INDOOR",
    },
    "Route16FuchsiaSpeechHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "Route16Gate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "Route7SaffronGate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "Route17Route18Gate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "Route40": {
        "tileset": TILESET_JOHTO,
        "type": "ROUTE",
    },
    "Route41": {
        "tileset": TILESET_JOHTO,
        "type": "ROUTE",
    },
    "CianwoodCity": {
        "tileset": TILESET_JOHTO,
        "type": "TOWN",
    },
    "ManiasHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "CianwoodGym": {
        "tileset": TILESET_TOWER,
        "type": "INDOOR",
    },
    "CianwoodPokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "CianwoodPharmacy": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "CianwoodPhotoStudio": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "CianwoodLugiaSpeechHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "PokeSeersHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "BattleTower1F": {
        "tileset": TILESET_BATTLE_TOWER_INSIDE,
        "type": "INDOOR",
    },
    "BattleTowerBattleRoom": {
        "tileset": TILESET_BATTLE_TOWER_INSIDE,
        "type": "INDOOR",
    },
    "BattleTowerElevator": {
        "tileset": TILESET_BATTLE_TOWER_INSIDE,
        "type": "INDOOR",
    },
    "BattleTowerHallway": {
        "tileset": TILESET_BATTLE_TOWER_INSIDE,
        "type": "INDOOR",
    },
    "Route40BattleTowerGate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "BattleTowerOutside": {
        "tileset": TILESET_BATTLE_TOWER_OUTSIDE,
        "type": "ROUTE",
    },
    "Route2": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "Route22": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "ViridianCity": {
        "tileset": TILESET_KANTO,
        "type": "TOWN",
    },
    "ViridianGym": {
        "tileset": TILESET_TRAIN_STATION,
        "type": "INDOOR",
    },
    "ViridianNicknameSpeechHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "TrainerHouse1F": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "TrainerHouseB1F": {
        "tileset": TILESET_FACILITY,
        "type": "INDOOR",
    },
    "ViridianMart": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "ViridianPokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "ViridianPokecenter2FBeta": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "Route2NuggetHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "Route2Gate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "VictoryRoadGate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "Route26": {
        "tileset": TILESET_JOHTO,
        "type": "ROUTE",
    },
    "Route27": {
        "tileset": TILESET_JOHTO,
        "type": "ROUTE",
    },
    "Route29": {
        "tileset": TILESET_JOHTO,
        "type": "ROUTE",
    },
    "NewBarkTown": {
        "tileset": TILESET_JOHTO,
        "type": "TOWN",
    },
    "ElmsLab": {
        "tileset": TILESET_LAB,
        "type": "INDOOR",
    },
    "PlayersHouse1F": {
        "tileset": TILESET_PLAYERS_HOUSE,
        "type": "INDOOR",
    },
    "PlayersHouse2F": {
        "tileset": TILESET_PLAYERS_ROOM,
        "type": "INDOOR",
    },
    "PlayersNeighborsHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "ElmsHouse": {
        "tileset": TILESET_PLAYERS_HOUSE,
        "type": "INDOOR",
    },
    "Route26HealHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "DayOfWeekSiblingsHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "Route27SandstormHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "Route29Route46Gate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "Route5": {
        "tileset": TILESET_KANTO,
        "type": "ROUTE",
    },
    "SaffronCity": {
        "tileset": TILESET_KANTO,
        "type": "TOWN",
    },
    "FightingDojo": {
        "tileset": TILESET_TRAIN_STATION,
        "type": "INDOOR",
    },
    "SaffronGym": {
        "tileset": TILESET_UNDERGROUND,
        "type": "INDOOR",
    },
    "SaffronMart": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "SaffronPokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "SaffronPokecenter2FBeta": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "MrPsychicsHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "SaffronMagnetTrainStation": {
        "tileset": TILESET_TRAIN_STATION,
        "type": "INDOOR",
    },
    "SilphCo1F": {
        "tileset": TILESET_FACILITY,
        "type": "INDOOR",
    },
    "CopycatsHouse1F": {
        "tileset": TILESET_PLAYERS_HOUSE,
        "type": "INDOOR",
    },
    "CopycatsHouse2F": {
        "tileset": TILESET_PLAYERS_HOUSE,
        "type": "INDOOR",
    },
    "Route5UndergroundPathEntrance": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "Route5SaffronGate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
    "Route5CleanseTagHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "Route30": {
        "tileset": TILESET_JOHTO,
        "type": "ROUTE",
    },
    "Route31": {
        "tileset": TILESET_JOHTO,
        "type": "ROUTE",
    },
    "CherrygroveCity": {
        "tileset": TILESET_JOHTO,
        "type": "TOWN",
    },
    "CherrygroveMart": {
        "tileset": TILESET_MART,
        "type": "INDOOR",
    },
    "CherrygrovePokecenter1F": {
        "tileset": TILESET_POKECENTER,
        "type": "INDOOR",
    },
    "CherrygroveGymSpeechHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "GuideGentsHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "CherrygroveEvolutionSpeechHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "Route30BerryHouse": {
        "tileset": TILESET_HOUSE,
        "type": "INDOOR",
    },
    "MrPokemonsHouse": {
        "tileset": TILESET_FACILITY,
        "type": "INDOOR",
    },
    "Route31VioletGate": {
        "tileset": TILESET_GATE,
        "type": "GATE",
    },
}