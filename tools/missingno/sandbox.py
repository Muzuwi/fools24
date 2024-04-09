import string
import hexdump
import differential
import pokechars


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

    dump(sprite1, "sandbox_sprite1")
    dump(sprite2, "sandbox_sprite2")
    dump(overlapping, "sandbox_overlap")
    dump(xord, "sandbox_xord")
    dump(unclobbered_xord, "sandbox_a6d0_a858")

    print(" === RE-ENCODING CHUNK 1 ===")
    encoder = differential.DifferentialEncoder(sprite1, MISSINGNO_SIZE[0], MISSINGNO_SIZE[1])
    sprite1_encoded = encoder.encode()
    hexdump.hexdump(sprite1_encoded, base=0x188)
    dump(sprite1_encoded, "sandbox_sprite1_reencoded")

    print(" === REPLACING CORRUPTED PARTS OF CHUNK 2 === ")
    uncorrupted_sprite2 = bytearray(sprite2[:])
    uncorrupted_sprite2[0x0:(0xA6D0-0xA310)] = sprite1_encoded[(0xA310-0xA188):(0xA6D0-0xA188)]
    uncorrupted_sprite2[(0xA6D0-0xA310):(0xA858-0xA310)] = unclobbered_xord
    hexdump.hexdump(uncorrupted_sprite2)
    dump(uncorrupted_sprite2, "sandbox_sprite2_uncorrupted")

    print(" === RE-ENCODING CHUNK 2 === ")
    encoder = differential.DifferentialEncoder(uncorrupted_sprite2, MISSINGNO_SIZE[0], MISSINGNO_SIZE[1])
    recovered = encoder.encode()
    hexdump.hexdump(recovered, base=0x310)
    dump(recovered, "sandbox_sprite2_recovered")

    print(" === GENERATING UPDATED SAVE FILE === ")
    new_data = bytearray(data[:])
    new_data[0x310:0x858] = recovered
    with open("welcome_back_missingno.sav", "wb") as f:
        f.write(new_data)
    print("Done!")

    print("Flag: ", pokechars.depokeify(new_data[0x7D7:0x7ED]))



if __name__ == "__main__":
    main()
