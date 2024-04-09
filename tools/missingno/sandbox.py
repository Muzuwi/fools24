import string
import hexdump
import differential


MISSINGNO_SIZE = (104, 104)
OVERFLOW_SIZE = (MISSINGNO_SIZE[0] // 8) * MISSINGNO_SIZE[1]


def dump(b: bytes, n: str):
    with open(n+".bin", "wb") as f:
        f.write(b)


def bruteforce_for_group(g: list[int]):
    """ Find an initial starting value for the bytes
    """



    print("Forcing", g)


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
    unclobbered_xord = xord[0x3C0:]
    hexdump.hexdump(unclobbered_xord, base=0x6D0)

    ptr = 0x310
    ptr_cached = 0x310
    x = 0
    y = 0
    file = open("logs.txt", "wt")
    statelist = []
    curlist = []
    mx = 0
    while True:
        file.write("%04x %d %d\n" % (0xA000+ptr, x, y))
        if ptr >= 0x6D0:
            curlist.append(ptr)
        mx = max(mx, ptr)

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
    print(f"Max ptr: {mx:04x}")

    for v in statelist:
        b = []
        print("State group:")
        for l in v:
            print(f"\tTarget: {0xA000+l:04x} | Offset from 0xA6D0: {l-0x6D0:04x}")
            b.append(unclobbered_xord[l - 0x6D0])

        bruteforce_for_group(b)

    SIZE = len(B"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x0C\x00\x37\x0F\x14\x02\x04\x09\x11\x22\x44\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x30\x30\x08\x10\x61\x00\x02\x08\x00\x01\xA0\x01\xA0\x49\x90\x20\x20\x40\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x21\x80\x00\x00\x00\x20\x48\x13\x45\x4C\x20\x40\x00\x04\x0A\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x30\x90\x40\x40\x40\x40\x40\x80\x00\x10\xF0\xA0\xA0\x00\x80\x80\x40\xC0\xC0\x80\x00\x00\x00\x00")
    TEST_INPUT = b"\x00\xFF\x00\xFF" * (SIZE // 4)
    diff = differential.DifferentialDecoder(
        TEST_INPUT,
        32, 32, invert=False)
    dump(TEST_INPUT, "sandbox_diff_in")
    dump(diff.decode(), "sandbox_diff_out")






    print(statelist)





    dump(sprite1, "sandbox_sprite1")
    dump(sprite2, "sandbox_sprite2")
    dump(overlapping, "sandbox_overlap")
    dump(xord, "sandbox_xord")
    dump(unclobbered_xord, "sandbox_a6d0_a858")




if __name__ == "__main__":
    main()
