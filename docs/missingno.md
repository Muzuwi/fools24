# missingno

```
00:a000 sSpriteBuffer0
00:a188 sSpriteBuffer1
00:a310 sSpriteBuffer2
00:a598 sHallOfFame
```

- testing on missingno `0xA1`
- `_UncompressSpriteData` uses `sSpriteBuffer1`
- `SPRITEBUFFERSIZE` = 7 * 7 * 1 * 8

- Input sprite

SpriteInputBitCounter=1
SpriteOutputBitOffset=3
SpritePosX=0
SpritePosY=0
SpriteLoadFlags=0

ReadNextInputByte - simply read next byte from wSpriteInputPtr and advance it
 

0xB8 -> C=1, 0x71

- ScaleSpriteByTwo


- D0B8 - wMonHIndex
- D0C3 - **wMonHFrontSprite**

- GetMonHeader

Mon data copied from:
- BaseStats + $1C * (dex_id[mon_id] - 1)
- $43DE + $1C * (dex_id[mon_id] - 1)
0x1C bytes copied to: $D0B8
from: $5FC2    (0026+BikerData)

(this will most definitely differ between language versions, below for pokered en)
missingno data: 002188001D0606001D8F880019378F37378F001A37370D37001C0D0D
front sprite: $1900 (thankfully in ROM0)
back sprite: $8F73

- RLE corruption could be restored? It only or's the bits in hall of fame data
- Unpack corruption seems awful and unrecoverable


RLE CORRUPTION: individual bits in HoF
DIFFERENTIAL DECODER CORRUPTION: 1352 bytes past $A310; last corrupted byte at $A857

