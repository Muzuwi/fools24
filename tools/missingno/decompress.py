import os
import sys
import utils


BLASTOISE = b"\x44\xB8\x55\x55\x57\xCE\x37\xAD\xAD\xA0\x8E\x35\x15\x05\x21\x39\x7B\x98\x56\x36\x7D\x5E\x61\xC3\x81\x68\xD9\xA9\x46\x88\x63\x82\xA3\x48\xA8\xD2\x89\x52\x11\x49\x4E\x54\x84\xA4\xE7\x61\x69\x8D\xE8\x94\x87\x22\x38\x55\x05\x2A\xA1\x4E\x2E\x21\x09\x42\xD5\x37\x50\x59\xDD\xEF\xAD\xF3\x5A\x30\xA8\xBA\x3C\x5D\xC2\x99\xA7\x2C\x38\x24\x31\xCF\x83\xA0\xC2\x9D\x1E\x10\x2C\x71\xA5\x41\x30\xB1\xB7\x83\x15\x04\x0D\x1C\x51\x31\x51\xCE\x84\x28\x20\x9C\x91\x28\x28\x27\x2C\x4C\x08\xC7\x64\x0E\x43\x1C\x49\x7A\x55\xA9\xBC\xAA\xC3\xD0\x53\xF1\xAE\x98\x3D\x1F\x18\x77\xBE\x3D\xF9\x3A\xD3\x9D\xE0\xAB\xD4\xE5\x7A\x39\x54\x18\x29\x6B\xB4\xD1\x7E\x41\x38\x5F\xED\x81\xA9\x0A\x90\xA3\x06\xA8\x65\x4E\x0A\x23\x22\x2E\xA1\x42\x25\xE9\x48\x42\x38\x7A\xA3\x2A\x21\x88\x97\x89\xA6\x15\x37\xA9\x26\x05\x21\x41\x8A\x60\x49\x62\x96\x36\xF5\x06\x7B\xBD\x0E\x25\x76\x07\xD8\xE1\x7D\x5D\x76\x26\xB4\x2C\x7E\x86\x9C\x88\x25\x06\xA3\x1A\x08\x21\xA2\xD5\x45\x06\xB4\xB8\x53\x08\xC5\xEF\x8D\x69\x60\x49\xA3\x04\x11\x41\x41\x29\xE2\xD5\x5A\xFB\xA0\x58\xA4\x25\x82\x2A\x29\x25\x45\x5B\xD6\x91\x88\xA9\x04\x87\x60\xE2\x96\x0D\x25\x21\x5D\x06\x30\x98\xBA\x46\xC2\x47\x05\x8B\x4C\xA8\x63\x65\x26\x2B\x09\x04\x22\x14\xCA\x3B\x10\x61\x76\x31\x99\x48\x4E\x9A\x14\x23\x65\x0C\x17\xA5\x8E\x9A\x8D\x54\x66\x70\xD7\x94\xE7\x58\xD1\xA6\x30\xAA\x05\x8E\x47\xCB\x6A\xA0\xA6\x38\x15\x38\xFD\x15\xA2\x17\x96\xA4\x50\x8C\xA3\x81\x07\x82\xA2\x90\x88\x55\xA1\x4E\xBA\xB4\xC1\x77\x52\x35\x53\xAD\x75\x05\x25\xAA\x22\x25\x48\xC8\x8E\x37\xE8\x68\x57\x86\x34\xBF\x6A\x39\x15\x55\xAF\xA0\x98\xF2\x6A\xA9\x8F\x2A\x7E\x10\x82\x9E\x9B\xC3\x7A\xA7\x2B\x9C\x5A\xA1\x51\x55\x10\x9C\x34\x72\xD4\x64\xAB\xF9\xA2\xF8\xA7\x0A\x44\xC6\x18\xFF\xF9\x83\xED\xED\x9C\x35\xA3\x18\x5F\xFF\xCE\x82\xFF\xF8\x47\x36\x31\x9D\x50\x35\xC4\x55\xFC\x72\x53\x16\x8A\x98\x7E\x92\x90\x91\x9A\x38\x26\x94\xFE\x0F\xA1\xFF\xE0\xF8\xB8\xF9\xAB\xC4\xAA\xBF\xFF\xCF\xFE\x1F\xF8\x7C\xFC\xBC\x68\xAF\xF5\x51\x35\x2F\xFF\xC1\x56\x1F\x87\xE1\xF9\x8A\xF5\x18\x59\x6D\x5F\xC0\xC0\xE3\xFB\x7E\xC6\x34\x31\xC2\xF8\x3E\x38\x40\x8B\x7E\x1F\xC9\xD7\x03"
UNIMPLEMENTED = RuntimeError("Unimplemented")


class Decompressor():
    LENGTH_ENCODING_OFFSET_LIST = [
        0x01,0x00,0x03,0x00,0x07,0x00,0x0F,0x00,0x1F,0x00,0x3F,0x00,0x7F,0x00,0xFF,0x00,0xFF,0x01,0xFF,0x03,0xFF,0x07,0xFF,0x0F,0xFF,0x1F,0xFF,0x3F,0xFF,0x7F,0xFF,0xFF
    ]


    def __init__(self, sprite: bytes) -> None:
        self.reader = utils.ByteReader(sprite)
        # available SRAM space starting from sSpriteBuffer1
        self.output = bytearray(b'\x00' * (0xC000 - 0xA000))
        self.output_ptr = None
        self.output_bit_offset = 0
        self.cur_pos_y = 0
        self.cur_pos_x = 0


    def print_state(self):
        print(f"==========================================")
        print(f"OutputPtr: {0xA000+self.output_ptr:04x}")
        print(f"OutputBitOffset: {self.output_bit_offset}")
        print(f"CurPosX: {self.cur_pos_x}")
        print(f"CurPosY: {self.cur_pos_y}")
        print(f"Output: {self.output}")


    def write_output(self, bits: int):
        b = self.output[self.output_ptr]
        b = (b & ~(0b00000011 << (self.output_bit_offset*2))) | ((bits & 0b00000011) << (self.output_bit_offset*2))
        self.output[self.output_ptr] = b


    def move_to_next_buffer_position(self) -> bool:
        self.cur_pos_y += 1
        if self.cur_pos_y >= self.height:
            # curColumnDone
            self.cur_pos_y = 0
            if self.output_bit_offset != 0:
                self.output_bit_offset -= 1
                self.output_ptr = self.output_ptr_cached
                return

            # bitOffsetsDone
            self.output_bit_offset = 3
            self.cur_pos_x += 8
            if self.cur_pos_x >= self.width:
                # allColumnsDone
                # this does cursed things with the stack
                self.cur_pos_x = 0
                return True

            self.output_ptr += 1
            self.output_ptr_cached = self.output_ptr
        else:
            self.output_ptr += 1

        return False


    def read_rl_encoded_zeros_count(self) -> int:
        zero_count = 0

        while True:
            if self.reader.read_bit() == 0:
                break
            zero_count += 1

        print("Zeros:", zero_count)
        offset = self.LENGTH_ENCODING_OFFSET_LIST[zero_count * 2] | (self.LENGTH_ENCODING_OFFSET_LIST[zero_count * 2 + 1] << 8)
        print("Offset:", offset)

        num_of_zeros = 0
        for _ in range(0, zero_count+1):
            num_of_zeros <<= 1
            num_of_zeros |= self.reader.read_bit()
        print(f"{num_of_zeros:x}")

        iterations = num_of_zeros + offset
        return iterations


    def decompress(self) -> bytearray:
        sizebyte = self.reader.read_byte()
        self.width = (sizebyte & 0xF) * 8
        self.height = ((sizebyte >> 4) & 0xF) * 8
        print(f"Sprite dimensions: {self.width}, {self.height}")

        self.flags = self.reader.read_bit()
        print(f"Starting flags: {self.flags:x}")
        self.output_bit_offset = 3

        while True:
            self.output_ptr = 0x188
            if self.flags & 0x1:
                self.output_ptr = 0x310
            self.output_ptr_cached = self.output_ptr
            print(f"Offset: {self.output_ptr:x}")

            # read unpacking mode when this is the last sprite
            if self.flags & 0x2:
                if self.reader.read_bit() == 0:
                    self.unpacking_mode = 0
                else:
                    self.unpacking_mode = 1 + self.reader.read_bit()
                print("Unpacking mode:", self.unpacking_mode)

            # if first bit is 0, input starts with zeros
            # handle this case
            if self.reader.read_bit() == 0:
                count = self.read_rl_encoded_zeros_count()
                for _ in range(0, count):
                    # write '00'
                    self.write_output(0b00)
                    if self.move_to_next_buffer_position():
                        break

            should_stop = False
            while not should_stop:
                self.print_state()

                mode = (self.reader.read_bit()<<1) | self.reader.read_bit()
                if mode == 0b00:
                    count = self.read_rl_encoded_zeros_count()
                    for _ in range(0, count):
                        # write '00'
                        self.write_output(0b00)
                        should_stop = self.move_to_next_buffer_position()
                        # this breaks from the inner for, not the while
                        if should_stop:
                            break
                else:
                    # simply send the bits to the output
                    self.write_output(mode)
                    should_stop = self.move_to_next_buffer_position()

            print("POST RLE:")
            # post RLE run, after all rows/columns are done
            # if this was the last sprite, exit
            if self.flags & 0b10:
                break

            # there's one more sprite to decompress, set flag and continue
            # after the next iteration is done, move on to UnpackSprite
            self.flags ^= 0b01
            self.flags |= 0b10

        # - UnpackSprite
        print("UNPACK SPRITE WITH MODE:", self.unpacking_mode)
        raise UNIMPLEMENTED
        return self.output


def main():
    decomp = Decompressor(BLASTOISE)
    print(decomp.decompress())


if __name__ == "__main__":
    main()




