DECODE_NYBBLE0_TABLE = [ 0x01,0x32,0x76,0x45,0xfe,0xcd,0x89,0xba ]
DECODE_NYBBLE1_TABLE = [ 0xfe,0xcd,0x89,0xba,0x01,0x32,0x76,0x45 ]
DECODE_NYBBLE0_FLIPPED_TABLE = [ 0x08,0xc4,0xe6,0x2a,0xf7,0x3b,0x19,0xd5 ]
DECODE_NYBBLE1_FLIPPED_TABLE = [ 0xf7,0x3b,0x19,0xd5,0x08,0xc4,0xe6,0x2a ]
ENCODE_NYBBLE0_TABLE = [ 0x01, 0x32, 0x67, 0x54, 0xcd, 0xfe, 0xab, 0x98 ]
ENCODE_NYBBLE1_TABLE = [ 0x89, 0xba, 0xef, 0xdc, 0x45, 0x76, 0x23, 0x10 ]

class DifferentialDecoder():
    def __init__(self,
                 input: bytes,
                 width: int,
                 height: int,
                 table0 = DECODE_NYBBLE0_TABLE,
                 table1 = DECODE_NYBBLE1_TABLE,
                 invert = False) -> None:
        self.buffer_size = (width // 8) * height
        if len(input) != self.buffer_size:
            raise RuntimeError(f"Invalid size for differential input, expected {self.buffer_size} bytes")
        self.input = input
        self.width = width
        self.height = height
        self.table_0 = table0
        self.table_1 = table1
        self.invert = invert
        self.previous_data = 0


    def decode_nybble(self, nybble: int) -> int:
        # print(f"PREVIOUS DATA: {self.previous_data:02x}")

        if self.invert:
            initial = self.previous_data & 0b1000
            print(f"decode_nybble: {self.previous_data} & 0b1000 = {initial}")
        else:
            initial = self.previous_data & 0b0001
            print(f"decode_nybble: {self.previous_data} & 0b0001 = {initial}")

        if initial == 0:
            table = self.table_0
            print(f"decode_nybble: table = self.table_0, as initial = 0 | {table}")
        else:
            table = self.table_1
            print(f"decode_nybble: table = self.table_1, as initial = 1 | {table}")

        print(f"decode_nybble: New nybble will be at table byte {nybble >> 1}, {'high' if nybble % 2 == 0 else 'low'} nybble")

        byte = table[nybble >> 1]
        if nybble % 2 == 0:
            new_nybble = (byte >> 4) & 0xF
        else:
            new_nybble = byte & 0xF
        print(f"decode_nybble: New nybble is {new_nybble:01x}")

        self.previous_data = new_nybble
        return self.previous_data


    def decode(self) -> bytearray:
        output = bytearray(b'\x00' * self.buffer_size)

        ptr = 0
        ptr_cached = 0
        x = 0
        y = 0
        while True:
            byte = self.input[ptr]
            high = (byte >> 4) & 0xF
            low = byte & 0xF

            print(f"byte[{ptr:04x}] = {high:01x} {low:01x}")

            # print(f"->[{ptr:04x}] HI: {high:02x} LO: {low:02x}")

            high = self.decode_nybble(high)
            low = self.decode_nybble(low)

            output[ptr] = (high << 4) | low
            print(f"byte[{ptr:04x}] = {output[ptr]:02x}")
            # print(f"-> OUTPUT[{ptr:04x}] = {output[ptr]:02x}")
            ptr += self.height

            x += 8
            if x >= self.width:
                print("clearing state")
                self.previous_data = 0
                x = 0
                y += 1
                if y >= self.height:
                    y = 0
                    break

                ptr_cached += 1
                ptr = ptr_cached

        return output


class DifferentialEncoder():
    def __init__(self,
                 b: bytes,
                 width: int,
                 height: int,
                 table0 = ENCODE_NYBBLE0_TABLE,
                 table1 = ENCODE_NYBBLE1_TABLE,
                 invert = False,
                 initial_data = 0) -> None:
        self.buffer_size = (width // 8) * height
        if len(b) != self.buffer_size:
            raise RuntimeError(f"Invalid size for input, expected {self.buffer_size} bytes but got {len(b)}")
        self.input = bytearray(b)
        self.width = width
        self.height = height
        self.table_0 = table0
        self.table_1 = table1
        self.invert = invert
        self.previous_data = initial_data


    def encode_nybble(self, nybble: int) -> int:
        initial = self.previous_data & 0b0001
        print(f"decode_nybble: {self.previous_data} & 0b0001 = {initial}")

        if initial == 0:
            table = self.table_0
            print(f"decode_nybble: table = self.table_0, as initial = 0 | {table}")
        else:
            table = self.table_1
            print(f"decode_nybble: table = self.table_1, as initial = 1 | {table}")

        print(f"decode_nybble: New nybble will be at table byte {nybble >> 1}, {'high' if nybble % 2 == 0 else 'low'} nybble")

        byte = table[nybble >> 1]
        if nybble % 2 == 0:
            new_nybble = (byte >> 4) & 0xF
        else:
            new_nybble = byte & 0xF
        print(f"decode_nybble: New nybble is {new_nybble:01x}")

        self.previous_data = nybble
        return new_nybble


    def encode(self) -> bytearray:
        output = bytearray(b'\x00' * self.buffer_size)

        ptr = 0
        ptr_cached = 0
        x = 0
        y = 0
        while True:
            byte = self.input[ptr]
            high = (byte >> 4) & 0xF
            low = byte & 0xF

            high = self.encode_nybble(high)
            low = self.encode_nybble(low)

            output[ptr] = (high << 4) | low

            ptr += self.height
            x += 8
            if x >= self.width:
                self.previous_data = 0
                x = 0
                y += 1
                if y >= self.height:
                    y = 0
                    break

                ptr_cached += 1
                ptr = ptr_cached

        return output
