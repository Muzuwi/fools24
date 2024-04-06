import sys

BASE = 0xC4A0
WIDTH = 20

v = sys.argv[1]
v = int(v, 16)

idx = (v - BASE)
x = idx % WIDTH
y = int(idx / WIDTH)

print("Coordinates:", x, ",", y)
print(f"(Screenshot coords: {x*8}, {y*8})")

