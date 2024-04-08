import string
import hexdump


MISSINGNO_SIZE = (104, 104)
OVERFLOW_SIZE = (MISSINGNO_SIZE[0] // 8) * MISSINGNO_SIZE[1]


def dump(b: bytes, n: str):
    with open(n+".bin", "wb") as f:
        f.write(b)


def main():
    with open("rest_in_miss_forever_ingno.sav", "rb") as f:
        data = f.read()

    # 0x188 - 0x6D0
    sprite1 = data[0x188:(0x188+OVERFLOW_SIZE)]
    # 0x310 - 0x858
    sprite2 = data[0x310:(0x310+OVERFLOW_SIZE)]
    overlapping = data[0x310:0x6D0]

    print(" === Hexdump of chunk 1 ===")
    hexdump.hexdump(sprite1, base=0x188)

    print(" === Hexdump of chunk 2 ===")
    hexdump.hexdump(sprite2, base=0x310)

    print(" === Hexdump of overlap ===")
    hexdump.hexdump(overlapping, base=0x310)

    print(" === CHUNK1 ^ CHUNK2 ===")
    xord = bytes(x ^ y for (x, y) in zip(sprite1, sprite2))
    hexdump.hexdump(xord, base=0x310)

    print(" === A6D0:A858 (1 ^ 2) ===")
    unclobbered_xord = xord[0x3D0:]
    hexdump.hexdump(unclobbered_xord, base=0x6D0)

    ptr = 0
    ptr_cached = 0
    x = 0
    y = 0
    file = open("logs.txt", "wt")
    statelist = []
    curlist = []
    while True:
        file.write("%04x %d %d\n" % (0xA310+ptr, x, y))
        if ptr >= (0x6D0 - 0x310):
            curlist.append(ptr)

        ptr += MISSINGNO_SIZE[1]

        x += 8
        if x >= MISSINGNO_SIZE[0]:
            file.write("# CLEAN STATE\n")
            statelist.append(curlist.copy())
            curlist = []
            x = 0
            y += 1
            if y >= MISSINGNO_SIZE[1]:
                y = 0
                break

            ptr_cached += 1
            ptr = ptr_cached
    file.close()

    for v in statelist:
        print("State group:")
        for l in v:
            print(f"\t{0xA310+l:04x}")


    print(statelist)





    dump(sprite1, "sandbox_sprite1")
    dump(sprite2, "sandbox_sprite2")
    dump(overlapping, "sandbox_overlap")
    dump(xord, "sandbox_xord")
    dump(unclobbered_xord, "sandbox_a6d0_a858")




if __name__ == "__main__":
    main()
