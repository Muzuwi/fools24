import pytest
import utils


def test_read_bits():
    stream = b'\xA0\xA0'
    reader = utils.ByteReader(stream)

    assert reader.read_bit() == 0x1, "bit0 == 1"
    assert reader.read_bit() == 0x0, "bit1 == 0"
    assert reader.read_bit() == 0x1, "bit2 == 1"
    assert reader.read_bit() == 0x0, "bit3 == 0"
    assert reader.read_bit() == 0x0, "bit4 == 0"
    assert reader.read_bit() == 0x0, "bit5 == 0"
    assert reader.read_bit() == 0x0, "bit6 == 0"
    assert reader.read_bit() == 0x0, "bit7 == 0"
    assert reader.read_bit() == 0x1, "bit8 == 1"
    assert reader.read_bit() == 0x0, "bit9 == 0"


def test_read_bytes():
    stream = b'\x00\x01\x02\x03'
    reader = utils.ByteReader(stream)

    assert reader.read_byte() == 0x00, "byte0 == 0x00"
    assert reader.read_byte() == 0x01, "byte1 == 0x01"
    assert reader.read_byte() == 0x02, "byte2 == 0x02"
    assert reader.read_byte() == 0x03, "byte3 == 0x03"


def test_read_bits_and_bytes():
    stream = b'\x00\xA0\xFF\xDA'
    reader = utils.ByteReader(stream)

    assert reader.read_byte() == 0x0, "byte0 == 0x0"
    assert reader.read_bit() == 0x1, "byte1.bit0 == 0x1"
    assert reader.read_bit() == 0x0, "byte1.bit1 == 0x0"
    assert reader.read_bit() == 0x1, "byte1.bit2 == 0x1"
    assert reader.read_bit() == 0x0, "byte1.bit3 == 0x0"
    assert reader.read_bit() == 0x0, "byte1.bit4 == 0x0"
    assert reader.read_bit() == 0x0, "byte1.bit5 == 0x0"
    assert reader.read_bit() == 0x0, "byte1.bit6 == 0x0"
    assert reader.read_bit() == 0x0, "byte1.bit7 == 0x0"
    assert reader.read_byte() == 0xFF, "byte2 == 0xFF"
    assert reader.read_bit() == 0x1, "byte3.bit0 == 0x1"
    assert reader.read_bit() == 0x1, "byte3.bit1 == 0x1"
    with pytest.raises(RuntimeError):
        assert reader.read_byte()
