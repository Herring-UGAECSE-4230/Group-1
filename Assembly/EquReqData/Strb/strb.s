.global _start

_start:
	MOV R1, #0x99
	LDR R6, =data_store
	STRB R1, [R6]

	ADD R6, R6, #1
	MOV R1, #0x85 
	STRB R1, [R6]
	
	ADD R6, R6, #1
	MOV R1, #0x3f
	STRB R1, [R6]
	
	ADD R6, R6, #1
	MOV R1, #0x63
	STRB R1, [R6]

	ADD R6, R6, #1
	MOV R1, #0x12
	STRB R1, [R6]

	LDRB  R2,[R6]
	LDRB  R3,[R6]

 	LDR R3, [R6]
  	SUB R6, R6, #4
   	LDR R2, [R6]
	MOV R7, #1
	SVC 0

.data
data_store: .space 8
