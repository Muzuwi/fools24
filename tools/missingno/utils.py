

class ByteReader():
    b: bytes
    ptr: int

    def __init__(self, b: bytes) -> None:
        self.b = b
        self.ptr = 0

    def read_bit(self) -> int:
        """ Read a single bit from the input
        """
        if self.ptr > 8 * len(self.b):
            raise RuntimeError("EOF reached")

        byteoffs = self.ptr // 8
        bitoffs = self.ptr % 8

        byte = self.b[byteoffs]
        value = (byte >> (7-bitoffs)) & 0x1
        self.ptr += 1

        return value


    def read_byte(self) -> int:
        """ Reads a byte
        """
        if self.ptr % 8 != 0:
            raise RuntimeError("Not all bits of the current byte have been read yet")
        if self.ptr > 8 * len(self.b):
            raise RuntimeError("EOF reached")
        if (self.ptr + 8) > 8 * len(self.b):
            raise RuntimeError("EOF reached")

        value = self.b[self.ptr // 8]
        self.ptr += 8
        return value
