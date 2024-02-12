val1 .req r1
val2 .req r2 
sum .req r0
	.text
	.global _start
_start:
	MOV val1, #0x25
	MOV val2, #0x34
	ADD sum, val1, val2
	MOV R7, #1
	SVC 0
