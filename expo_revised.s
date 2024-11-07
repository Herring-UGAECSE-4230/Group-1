    .text
    .global main

main:
    PUSH {LR}
    @ Prompt and input x (floating-point)
    ldr r0, =msg_enter_x
    bl printf
    ldr r0, =fmt_float
    ldr r1, =x_val
    bl scanf
    @ Prompt and input n (integer)
    ldr r0, =msg_enter_n
    bl printf
    ldr r0, =fmt_int
    ldr r1, =n_val
    bl scanf
    @ Load x and n
    vldr s0, [x_val]         @ Load x (float) to s0
    ldr r3, [n_val]          @ Load n to r3
    @ Initialize result in s1 to 1.0
    vmov.f32 s1, #1.0
    cmp r3, #0               @ If n == 0, skip calculation
    beq print_result
power_loop:
    vmul.f32 s1, s1, s0      @ result *= x
    subs r3, #1              @ n -= 1
    bne power_loop           @ Repeat until n == 0
print_result:
    vcvt.f64.f32 d0, s1      @ Convert result to double
    vmov r1, r2, d0          @ Load result for printf
    ldr r0, =fmt_output
    bl printf
    POP {PC}                 @ Return
    MOV, PC, LR

.data
x_val:        .word 0                       @ Storage for x
n_val:        .word 0                       @ Storage for n
msg_enter_x:  .asciz "Calculate x^n. Enter x: "
msg_enter_n:  .asciz "Enter n: "
fmt_output:   .asciz " = %f\n"
fmt_int:      .asciz "%d"
fmt_float:    .asciz "%f"
