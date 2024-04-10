#!/usr/bin/env bash

# using "modern" build ELF for symbols because the classic one throws dwarf errors
# while the modern build is not even the same hash and literally the entire ROM is
# different outside of the header, surely this won't break..
/opt/devkitpro/devkitARM/bin/arm-none-eabi-gdb \
	../../extern/pokeemerald/pokeemerald_modern.elf \
	-ex "target remote :2346" \
	-ex "layout split" \
	-ex "break *0x08175620" \
	-ex "break *0x08175621"
