.text
.p2align 2
.globl _peer_pin
_peer_pin:
    // Original verifier has already fetched the dispatcher's signing identifier.
    // X19 = default allocator; X20 = expected identifier C string; X21 = actual identifier.
    // [SP] is the retained SecCodeCopySigningInformation dictionary.
    mov x0, x19
    mov x1, x20
    mov w2, #0x100
    movk w2, #0x800, lsl #16
    .long 0xdead0001 // CFStringCreateWithCString
    mov x20, x0
    cbz x20, L_no_key
    mov x0, xzr
    adr x1, L_unique
    mov w2, #0x100
    movk w2, #0x800, lsl #16
    .long 0xdead0002 // CFStringCreateWithCString
    mov x19, x0
    cbz x19, L_no_key
    ldr x0, [sp]
    mov x1, x19
    .long 0xdead0003 // CFDictionaryGetValue
    mov x22, x0
    cbz x22, L_bad
    mov x0, x22
    .long 0xdead0004 // CFDataGetLength
    cmp x0, #20
    b.ne L_bad
    mov x0, x22
    .long 0xdead0005 // CFDataGetBytePtr
    cbz x0, L_bad
    adr x1, L_digest
    mov x2, #20
    .long 0xdead0006 // memcmp
    cbnz w0, L_bad
    mov x0, x20
    mov x1, x21
    mov x2, xzr
    .long 0xdead0007 // CFStringCompare
    cmp x0, #0
    csetm w22, ne
    .long 0xdead0008 // branch to original cleanup at 0x100974508
L_bad:
    mov w22, #-1
    .long 0xdead0009 // branch to original cleanup at 0x100974508
L_no_key:
    mov x19, xzr
    mov w22, #-1
    .long 0xdead000a // branch to original cleanup at 0x100974510
.p2align 2
L_unique:
    .asciz "unique"
.p2align 2
L_digest:
    .byte 0xb2,0xc3,0x7d,0xa2,0xa3,0x04,0x3d,0x38,0x8d,0xa2
    .byte 0x69,0x6e,0xa9,0x05,0xa2,0xac,0xad,0x23,0x76,0x9e
