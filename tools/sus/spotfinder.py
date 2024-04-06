import sys
import struct
import rgbbin.objfile
from map_tileset_data import MAP_TO_TILESET_DATA

MAP_DATA_OBJ = "map_data.o"
TILESET_DATA_OBJ = "tilesets.o"


def parse_attributes(obj: rgbbin.objfile.ObjectFile, name: str):
    attr_sym = obj.symbol_by_name(f"{name}_MapAttributes")
    if attr_sym is None:
        raise RuntimeError(f"No attribute data found for {name}")

    sectid = attr_sym["sectid"]
    sect = obj.section_by_id(sectid)

    off = attr_sym["value"]
    data = sect["data"][off:off+3]
    print(data)

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
            print(attrs)
            print(blocks)

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

        print(blkdata, width, height, tileset_name, tileset)
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


def main():
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

        print(f"Associated tileset:")
        print(f"\t{tilesets[MAP_TO_TILESET_DATA[k]['tileset']]}")

        print(f" ===== {k} ===== ")
        tile_width = tilemaps[k]["width"]
        tile_height = tilemaps[k]["height"]
        tilemap = tilemaps[k]["tiles"]
        for y in range(0, tile_height):
            for x in range(0, tile_width):
                print(f"{tilemap[y*tile_width+x]:x}".zfill(2), " ", end="")
            print()
        print(f" =============== ")

    return




if __name__ == "__main__":
    main()

