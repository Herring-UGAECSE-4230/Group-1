    .text
    .global main

main:
    PUSH {LR}

    @ PRINT INITIAL MESSAGE
    ldr r0, =display       @ Setup printf for initial message
    bl printf              @ Print "Enter n!: "

    @ SCAN
    ldr r0, =float         @ Setup scanf for integer input
    ldr r1, =int
    bl scanf               @ Scan user input and store in `int`

    @ Load input value
    ldr r1, =int           @ Load input address
    vldr s0, [r1]          @ Load input value into s0
    vmov.f32 s5, s0        @ Store original input value in s5 for printing

    @ Display "n! = ..." by printing `n` before calculating factorial
    vcvt.s32.f32 s2, s5    @ Convert original input to integer in s2
    vmov r1, s2            @ Move integer n from s2 to r1 for printf
    ldr r0, =numPart       @ Load format for integer part of output
    bl printf              @ Print "n"

    vmov.f32 s1, #1.0      @ Initialize result to 1 (for 0! case)
    vmov.f32 s4, #1.0      @ Load 1.0 into s4 for decrementing loop
    vmov.f32 s0, s5        @ Initialize s0 as a copy of original n for looping

    @ Convert and check if n == 0
    vcvt.s32.f32 s2, s0    @ Convert n to integer in s2
    vmov r3, s2            @ Move integer n from s2 to r3 for comparison
    cmp r3, #0             @ Check if input n is zero
    beq print_result       @ If input is zero, skip to print result as 1

    @ FACTORIAL LOOP for n > 0
factorial:
    vmul.f32 s1, s1, s0    @ result *= n
    vsub.f32 s0, s0, s4    @ n -= 1 by subtracting 1.0 in s4
    vcvt.s32.f32 s2, s0    @ Convert n to integer in s2
    vmov r3, s2            @ Move integer n from s2 to r3
    cmp r3, #0             @ Check if n == 0
    bne factorial          @ Continue loop if n > 0

print_result:
    vcvt.f64.f32 d0, s1    @ Convert result to double for printf
    ldr r0, =answer        @ Load format for final result
    vmov r1, r2, d0        @ Move result into printf arguments
    bl printf

    POP {PC}
    MOV PC, LR             @ Return from main

.data
display: .asciz "Enter n!: "
.align 4
answer: .asciz "! = %f\n"   @ Answer format with factorial result
int:    .word 0             @ Storage for input
float:  .asciz "%f"         @ Format for scanf
numPart: .asciz "%.0f"      @ Format to print integer n before "!"
