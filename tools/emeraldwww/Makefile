SDKPATH := /opt/devkitpro/devkitARM/bin/

default: payload.bin

clean:
	rm a.out || true
	rm payload.o || true
	rm payload.bin || true

payload.o: payload.c
	${SDKPATH}arm-none-eabi-gcc -c -mthumb payload.c -o payload.o

payload.bin: payload.o
	${SDKPATH}arm-none-eabi-objcopy -O binary payload.o payload.bin

hex-payload: payload.bin
	xxd -p payload.bin | fold -w2 | paste -sd' ' -

asm-payload: payload.o
	${SDKPATH}arm-none-eabi-objdump -d payload.o

