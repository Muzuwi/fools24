import string


def hexdump(b: bytes,
            width: int = 16,
            base: int = 0x0):
    length = len(b)

    ptr = 0
    while ptr < length:
        if ptr % width == 0:
            print(f"${base+ptr:04x}: ", end="")

        print(f"{b[ptr]:02x} ", end="")

        remain = length - ptr - 1
        if (ptr % width == (width - 1)) or remain == 0:
            count = (ptr % width) if remain == 0 else width

            print("| ", end="")
            for i in range(count, 0, -1):
                ch = chr(b[ptr - i + 1])
                if ch in string.printable and ch not in string.whitespace:
                    print(ch, end="")
                else:
                    print(".", end="")
            print()

        ptr += 1

    print()
