# Crystal sus file

haha amogus

# Save file

Trainer name seems weird?
Saving on a regular save, normal name is terminated with $50 ctrl char (and nulls in the other positions of the 11-char buffer)
In the save it's: $8C $84 $93 $53 $53 $53 $53 $53 $53 $38 $38    (end of 11-char buffer)  $38 $15 $00

MET<RIVAL><RIVAL><RIVAL><RIVAL><RIVAL><RIVAL><RED><RED>

Do functions handling trainer name check for:
- $50 terminator?
- null checked?

Interesting:
- If there is no bounds checking, then trainer name overflows into wMomsName (which contains null - does this terminate, or continue further?)

```
wPlayerName: 8C 84 93 53 53 53 53 53 53 38 38   ; MET<RIVAL><RIVAL><RIVAL><RIVAL><RIVAL><RIVAL><RED><RED> (unterminated! ends at wRivalName)
wMomsName  : 38 15 00 11 A3 12 42 4B C3 F6 DE   ; <map$38><MOBILE><NULL><map$11>d<map$12><map$42><implCONT><blank>0<blank> (unterminated! ends at wRivalName)
wRivalName : 4E 4E 4E 4E 4E 4E 4E 4E 50 50 00   ; <NEXT><NEXT><NEXT><NEXT><NEXT><NEXT><NEXT><NEXT> (terminated)
wRedsName  : D0 D0 22 D0 D0 22 D0 D0 22 50 50   ; <blank><blank><map$22><blank><blank><map$22><blank><blank><map$22> (terminated)
wGreensName: 22 22 22 22 50 50 50 50 50 50 CD   ; <map$22><map$22><map$22><map$22> (terminated)
```

# RunMobileScript

- Discovered funky stray rop-like hunks of executed code in WRAM using bgb logging mode (spray and pray reverse engineering lol)
- Tracing leads to RunMobileScript

_RunMobileScript - ld a, (de) where de=D48A - wMomsName!
$15 control character is <MOBILE>!

wPlayersName -> overflows onto wMomsName, executes <MOBILE>, which runs some sort of script?

Source location: [mobile_5f.asm](../extern/pokecrystal/mobile/mobile_5f.asm)

# Mobile script

- Terminates like a regular string ($50)
- Each (byte-1) is interpreted as a key to a jumptable
- Bytes > $10 terminate script processing
- **But byte=$00 passes the check - underflows to $FF**

```
15 (starting byte, included for clarity, not processed)

00 11 A3 12 42 4B C3 F6 DE 4E 4E 4E 4E 4E 4E 4E 4E

50 (ending byte in wRivalName)
```

5f:7061 _RunMobileScript.Jumptable

```
$7081
$70F8
$7154
$7181
$71D0
$7220
$727B
$72CB
$72FF
$7334
$7382
$73C9
$73F0
$741D
$744F
$744F
```

Script byte $00: pointer from $725F in ROM

**EXECUTION REDIRECTED TO: $CD52**

# The Payload

$CD52 - payload start

rets to wMomsName (address pushed by _RunMobileScript), then executes:
```
@D48B
ld de, 12A3  ; String_Space
ld b, d
ld c, e
jp wBreedMon1Nick
```
```
@DEF6

ld a, (C590)
cp a, 79
jr nz, DF42

ld a, (C4AB)
cp a, 5   ; $DF00: $FE
          ; $DF01: $05
jr nz, DF42

ld a, (C51F)
cp a, 23
jr nz, DF42

```
```
@DF42
ld hl, sp+08
ld c, (hl)
inc hl
ld b, (hl)
inc bc
inc bc
inc bc
ld h, b
ld l, c
ret

(BC=C577, return to RunMobileScript, which terminates as de=12A3, [de]=$50)
```

- [C590] = $79
- [C4AB] = $05
- [C51F] = $23
- [C4CB] = $02
- [C4CC] = $04
- [C588] = $01
- function_DF4D(a=0) = $35   ; presumably hash of the OAM


