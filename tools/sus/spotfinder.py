import sys
import struct
import rgbbin.objfile
from map_tileset_data import MAP_TO_TILESET_DATA

MAP_DATA_OBJ = "map_data.o"
TILESET_DATA_OBJ = "tilesets.o"
DEBUG_PRINT_MAPS_AND_EXIT = False


def parse_attributes(obj: rgbbin.objfile.ObjectFile, name: str):
    attr_sym = obj.symbol_by_name(f"{name}_MapAttributes")
    if attr_sym is None:
        raise RuntimeError(f"No attribute data found for {name}")

    sectid = attr_sym["sectid"]
    sect = obj.section_by_id(sectid)

    off = attr_sym["value"]
    data = sect["data"][off:off+3]
    # print(data)

    border_block, height, width = struct.unpack('BBB', data)
    return {
        "border_block": border_block,
        "width": width,
        "height": height,
    }


def get_block_data(obj: rgbbin.objfile.ObjectFile, name: str, attrs: dict):
    attr_sym = obj.symbol_by_name(f"{name}_Blocks")
    if attr_sym is None:
        raise RuntimeError(f"No attribute data found for {name}")

    sectid = attr_sym["sectid"]
    sect = obj.section_by_id(sectid)

    off = attr_sym["value"]
    count = attrs["width"] * attrs["height"]
    data = sect["data"][off:off+count]
    return data


def get_tilesets():
    tilesets = {}

    with rgbbin.objfile.ObjectFile(TILESET_DATA_OBJ) as obj:
        obj.parse_all()

        names = [
            x["name"].replace("Meta", "") for x in obj.symbols if x["name"].startswith("Tileset") and x["name"].endswith("Meta")
        ]
        for name in names:
            sym = obj.symbol_by_name(f"{name}Meta")
            sectid = sym["sectid"]
            sect = obj.section_by_id(sectid)

            off = sym["value"]
            # theoretically the data can be less than this and this also
            # partially overlaps consecutive tilesets, but it doesn't matter.
            count = 4 * 4 * 256
            data = sect["data"][off:off+count]
            # group by metatile index
            metatiles = list(zip(*(iter(data),) *16))

            tilesets[name] = {
                "metatiles": metatiles
            }

    return tilesets


def get_map_data():
    map_data = {}

    with rgbbin.objfile.ObjectFile(MAP_DATA_OBJ) as obj:
        obj.parse_all()

        maps = [x["name"].replace("_MapAttributes", "") for x in obj.symbols if "_MapAttributes" in x["name"]]
        print("Loaded %d maps from symbols in %s" % (len(maps), MAP_DATA_OBJ))

        for m in maps:
            print("Parsing map %s.." % m)
            attrs = parse_attributes(obj, m)
            blocks = get_block_data(obj, m, attrs)
            # print(attrs)
            # print(blocks)

            map_data[m] = {
                "attributes": attrs,
                "blocks": blocks,
            }

    return map_data


def generate_tile_maps(maps, tilesets):
    tilemaps = {}

    for k, m in maps.items():
        blkdata = m["blocks"]
        width = m["attributes"]["width"]
        height = m["attributes"]["height"]
        tileset_name = MAP_TO_TILESET_DATA[k]['tileset']
        tileset = tilesets[tileset_name]

        # print(blkdata, width, height, tileset_name, tileset)
        tilemap = []
        for y in range(0, height):
            # go one row at a time
            for lvl in range(0, 16, 4):
                for x in range(0, width):
                    idx = blkdata[y * width + x]
                    tiles = tileset["metatiles"][idx][lvl:(lvl+4)]
                    tilemap.extend(tiles)

        tilemaps[k] = {
            "tiles": tilemap,
            "width": width * 4,
            "height": height * 4
        }

    return tilemaps


REQUESTED_VALUES = [
    # tile_x, tile_y, tile_val
    # (0 , 12, 0x79), <- UI tile, not map
    (11, 0, 0x05),
    (7, 6, 0x23),
    (3, 2, 0x02),
    (4, 2, 0x04),
    # (12, 11, 0x01) <- also UI i think, removed it and found a match
]


def check_match(tilemap, x: int, y: int):
    width = tilemap["width"]
    height = tilemap["height"]

    matches = 0
    for r in REQUESTED_VALUES:
        target_x = x + r[0]
        target_y = y + r[1]
        wanted = r[2]
        if target_x >= width or target_y >= height:
            continue

        if tilemap["tiles"][target_y * width + target_x] == wanted:
            matches = matches + 1

    if matches > 1:
        print(f"[partial] Found {matches} matches at {target_x}, {target_y}")
    return matches == len(REQUESTED_VALUES)


def print_hex_list(data, width, height):
    for y in range(0, height):
        for x in range(0, width):
            print(f"{data[y*width+x]:x}".zfill(2), " ", end="")
        print()


def debug_print_maps():
    maps = get_map_data()
    tilesets = get_tilesets()
    tilemaps = generate_tile_maps(maps, tilesets)

    for k,m in maps.items():
        blkdata = m["blocks"]
        width = m["attributes"]["width"]
        height = m["attributes"]["height"]

        print(f" ===== {k} ===== ")
        for y in range(0, height):
            for x in range(0, width):
                print(f"{blkdata[y*width+x]:x}".zfill(2), " ", end="")
            print()
        print(f"Map dimensions: {width}x{height}")
        print(f"Map tileset: {MAP_TO_TILESET_DATA[k]['tileset']}")
        print_hex_list(blkdata, width, height)
        print(f"Associated tileset:")
        print(f"\t{tilesets[MAP_TO_TILESET_DATA[k]['tileset']]}")

        print(f" ===== {k} ===== ")
        tile_width = tilemaps[k]["width"]
        tile_height = tilemaps[k]["height"]
        tilemap = tilemaps[k]["tiles"]
        print_hex_list(tilemap, tile_width, tile_height)
        print(f" =============== ")


def main():
    if DEBUG_PRINT_MAPS_AND_EXIT:
        debug_print_maps()
        return


    maps = get_map_data()
    tilesets = get_tilesets()
    tilemaps = generate_tile_maps(maps, tilesets)

    for k, m in tilemaps.items():
        width = m["width"]
        height = m["height"]

        # the player can only move in increments of two GB tiles
        for y in range(0, height, 2):
            for x in range(0, width, 2):
                if not check_match(m, x, y):
                    continue

                # for r in REQUESTED_VALUES:
                #     print(m["tiles"][(y+r[1])*width + x + r[0]])

                map_x, map_y = int((x+8)/2), int((y+8)/2)
                print(f"SUCCESS: Found complete match at map {k}")
                print(f"In-map coordinates: {map_x},{map_y} (0-indexed)")
                print(f"In-map coordinates (hex): {map_x:02x},{map_y:02x}")
                print(f"Check 01:dcb8 and 01:dcb7 respectively for X/Y (wXCoord/wYCoord)")
                print_hex_list(m["tiles"], width, height)

    return




if __name__ == "__main__":
    main()

