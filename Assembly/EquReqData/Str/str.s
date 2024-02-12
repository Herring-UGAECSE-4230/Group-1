.text
.global _start

_start:
	LDR R0, =a 
	LDR R1, [R0]
	
	LDR R0, =b
	LDR R2, [R0]

	ADD R3, R1,R2
	LDR R0, =c
	STR R3, [R0]

	MOV R7, #1
	SVC 0

.data
a: .word 5
b: .word 4
c: .word 0
