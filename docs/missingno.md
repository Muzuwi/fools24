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



