.global _start

.equ GPIO_BASE, 0xFE200000
.equ GPFSEL2, 0x08

.equ GPIO_21_OUTPUT, 0x8 ;//# 1 << 3

.equ GPFSET0, 0x1c
.equ GPFCLR0, 0x28

.equ GPIOVAL, 0x200000 ;//# 1 << 21
.equ ON_TIME, 250000000
.equ OFF_TIME,750000000

#a set of instructions designated to convert the On and Off times into formats suitable for the delay loops
calc1:
	ldr r3, =ON_TIME #set r3 to have ON_TIME value
	ldr r4, =#312500  #set r4 to have 312500 which is the denominator in the ratio between 3200 and 1000000000
	mov r5, #0 # initialize updated ON_TIME register
	mov r6, #0 # initialize updated OFF_TIME register
inner1:
# subtracts r4 from r3 until a zero is reached or r3 is less than r4. r5 is incremented accordingly
	subs r3, r3, r4 
  beq extra1
	cmp r3,r4
	blt calc2
	add r5, r5, #1
	b inner1
calc2:
# this is the same procedure as before, but with OFF_TIME
	ldr r3, =OFF_TIME
inner2:
	subs r3, r3, r4
	beq extra2
	cmp r3, r4
	blt _start
	add r6, r6, #1
	b inner2 

 # these are instructions to increment r5 or r6 once more if subtracting r4 from r3 yields a 0
extra1:
	add r5, r5, #1
	b calc2
extra2: 
	add r6, r6, #1
	b _start
	
	

_start:
	
	
	;//# base of our GPIO structure
	ldr r0, =GPIO_BASE

	;//# set the GPIO 21 function as output
	ldr r1, =GPIO_21_OUTPUT
	str r1, [r0, #GPFSEL2]

	# set counter
	ldr r2, =0x800000

loop:

	# turn on the LED
	ldr r1, =GPIOVAL ;//# value to write to set register
	str r1, [r0, #GPFSET0] ;//# store in set register

	# Wait for some time, delay
	mov r9, r5     ;//# Adjust the number of repetitions
	mov r8, r5   ;//# Adjust the initial value for each chunk delay

delay_outer:
	mov r10, r8    ;//# Preserve the initial value for each chunk delay

delay_inner:
	subs r10, r10, #1
	bne delay_inner

	subs r9, r9, #1
	bne delay_outer



	# turn off the LED
	ldr r1, =GPIOVAL ;//# value to write to set register
	str r1, [r0, #GPFCLR0] ;//# store in set register

	# Wait for some time, delay
	mov r9, r6      ;//# Adjust the number of repetitions
	mov r8, r6   ;//# Adjust the initial value for each chunk delay

delay_outer1:
	mov r10, r8    ;//# Preserve the initial value for each chunk delay

delay_inner1:
	subs r10, r10, #1
	bne delay_inner1

	subs r9, r9, #1
	bne delay_outer1


	b loop
