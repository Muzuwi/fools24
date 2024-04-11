#include <stdint.h>
#include <stddef.h>

typedef void(*GetSetPokedexFlag_t)(uint16_t, uint8_t);
#define GSPFAddr (0x080c0664 | 1)

typedef void(*SaveGame_t)();
#define SGAddr (0x0809ff80 | 1)

void _payload()
{
	// bepis name
	*(uint8_t volatile*)(0x03005d90 + 0) = 0x42;
	*(uint8_t volatile*)(0x03005d90 + 1) = 0x45;
	*(uint8_t volatile*)(0x03005d90 + 2) = 0x50;
	*(uint8_t volatile*)(0x03005d90 + 3) = 0x49;
	*(uint8_t volatile*)(0x03005d90 + 4) = 0x53;
	*(uint8_t volatile*)(0x03005d90 + 5) = 0x00;
	// national dex
	*(uint8_t volatile*)(0x03005d90 + 0x18 + 0x2) = 0xDA;
	// starter mon
	*(uint8_t volatile*)(0x03005d8c + 0x139C + 0x23) = 0x2;
 
	// Set some mons as caught/seen
	for(size_t i = 0; i < 100; ++i) {
		// set seen and caught
		((GetSetPokedexFlag_t)GSPFAddr)(i, 2);
		((GetSetPokedexFlag_t)GSPFAddr)(i, 3);
	}

	// Doesn't work..
	// ((SaveGame_t)SGAddr)();
}
