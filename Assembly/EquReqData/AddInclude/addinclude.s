
.include "unistd.s"

.global _start

_start:
	MOV R1, #0x14
	ADD R0, R1, #0XA
	MOV R7, #1
	SWI 0
