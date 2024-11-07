    .text
    .global main

main:
    PUSH {LR}

    @ PRINT
    ldr r0, =display       @ Setup printf for initial message
    bl printf              @ Print "Enter n!: "

    @ SCAN
    ldr r0, =float         @ Setup scanf for integer input
    ldr r1, =int
    bl scanf               @ Scan user input and store in `int`

    @ Load input value
    ldr r1, =int           @ Load input address
    vldr s0, [r1]          @ Load input value into s0

    vmov.f32 s1, #1.0      @ Initialize result to 1 (in case of 0!)
    vcvt.s32.f32 s2, s0    @ Convert input to integer in s2
    vmov r3, s2            @ Move integer input from s2 to r3 for comparison
    cmp r3, #0             @ Check if input is zero
    beq print_result       @ If input is zero, skip to print result

    @ FACTORIAL LOOP for n > 0
factorial:
    vmul.f32 s1, s1, s0    @ result *= n
    vsub.f32 s0, s0, #1.0  @ n -= 1
    vcvt.s32.f32 s2, s0    @ Convert n to integer in s2
    vmov r3, s2            @ Move integer n from s2 to r3
    cmp r3, #0             @ Check if n == 0
    bne factorial          @ Continue loop if n > 0

print_result:
    vcvt.f64.f32 d0, s1    @ Convert result to double for printf
    ldr r0, =answer
    vmov r1, r2, d0        @ Move result into printf arguments
    bl printf

    POP {PC}
    MOV PC, LR             @ Return from main

.data
display: .asciz "Enter n!: "
.align 4
answer: .asciz "! = %f\n"

int:    .word 0             @ Storage for input
float:  .asciz "%f"         @ Format for scanf
numPart: .asciz "%.0f"      @ Format for integer display
