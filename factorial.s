	.text
	.global main

main:
	PUSH {LR}
	@PRINT
	ldr r0, =display	@sets up printf
	bl printf			@prints the starting message
	@SCAN
	ldr r0, =float		@sets up scanf
	ldr r1, =int
	bl scanf			@scan for user input to get n
	
	ldr r1, =int
	vldr s0, [r1]
	vcvt.f64.f32 d0, s0
	vmov r1, r2, d0
	ldr r0, =numPart
	bl printf
	ldr r0, =int
	vldr s0, [r0]
	vmov.f32 s4, #1
	vmov.f32 s1, #1
factorial:
	vmul.f32 s3,s0,s1		@Iteration of multiplying base by element
	vmov.f32 s1, s3			@Move answer
	vcmp.f32 s0, s4			@Set flags
	vsub.f32 s0, s0, s4		@Next iteration, subtract 1
	vmrs apsr_nzcv, fpscr	@Update fpscr with flags
	bne factorial			@Repeat until element is 0
	vcvt.f64.f32 d0, s1		
	ldr r0, =answer			
	vmov r1, r2, d0			
	bl printf
    POP {PC}
    MOV PC, LR
	
.data
display: .asciz "Enter n!: "
.align 4
answer: .asciz "! = %f\n"

int:	.word 0		
float:  .asciz "%f"	
numPart:  .asciz "%.0f"	
		
