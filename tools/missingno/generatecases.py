import differential
import random
import sys

DICTIONARY = [0x0, 0xff, 0xaa, 0x80]
SIZE = 32
COUNT = 10

encoder = True
if len(sys.argv) > 1 and sys.argv[1] == "--decoder":
    encoder = False

for i in range(0, COUNT):
    bytelen = (SIZE // 8) * SIZE
    data = bytes([random.choice(DICTIONARY) for _ in range(0, bytelen)])

    initial_data = 0x0
    decoder = differential.DifferentialDecoder(data, SIZE, SIZE)
    out = decoder.decode()

    if encoder:
        print(f"""
(
    "Random Mix $0/$FF/$AA/$80:",
    {bytes(out)},
    {data},
    {SIZE}, {SIZE}, {initial_data}
),""", end="")
    else:
        print(f"""
(
    "Random Mix $0/$FF/$AA/$80:",
    {data},
    {bytes(out)},
    {SIZE}, {SIZE}, False
),""", end="")

print()












