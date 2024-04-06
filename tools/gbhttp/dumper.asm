def STATUS_INIT            equ 0
def STATUS_WAITING_FOR_REQ equ 1
def STATUS_RECEIVED_REQ    equ 2
def STATUS_DONE            equ 3

SECTION "WRAM0", WRAM0[$C000]
_wRequestData:
    ds $800
wResponseData:
    ds $800

SECTION "HRAM", HRAM[$FF80]
hDriverStatus:
    ds 1

SECTION "ROM", ROM0[$0200]
DumperPayload:
    ld c, 255
    ld de, $41F0
    ld hl, wResponseData
.loop:
    ld a, [de]
    ld b, a

    swap a
    and $f
    add "0"
    ld [hli], a

    ld a, b
    and $f
    add "0"
    ld [hli], a

    inc de
    dec c
    jp nz, .loop
.done:
    ; Notify the harness that the job is finished
    ld a, STATUS_DONE
    ldh [hDriverStatus], a
.forever
    ld b, b
    jr .forever


