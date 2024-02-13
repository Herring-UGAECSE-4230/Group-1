.text
.global _start

_start:
	LDR R2, =our_fixed_data
	LDRB R0, [R2]
	MOV R7, #1
	SVC 0

our_fixed_data:
	.byte 0x55, 0x33, 1, 2, 3, 4, 5, 6
	.word 0x23222120, 0x30
	.hword 0x4540, 0x50

