    .text
    .global main

main:
    PUSH {LR}
    
    @ Prompt and input x value
    ldr r0, =msg_input_x       @ Display "Enter x:"
    bl printf
    ldr r0, =fmt_float_input   @ Floating-point format for x input
    ldr r1, =store_x
    bl scanf

    @ Prompt and input n value
    ldr r0, =msg_input_n       @ Display "Enter n:"
    bl printf
    ldr r0, =fmt_int_input     @ Integer format for n input
    ldr r1, =store_n
    bl scanf

    @ Load x and display initial values
    ldr r0, =store_x           @ Load address of x
    vldr s2, [r0]              @ Load x into s2
    vcvt.f64.f32 d2, s2        @ Convert x to double
    vmov r1, r2, d2            @ Move to display registers
    ldr r0, =fmt_float_display @ Display x value
    bl printf

    @ Display n as exponent part
    ldr r0, =store_n
    ldr r1, [r0]               @ Load integer n from memory
    ldr r0, =fmt_exp_display   @ Format for displaying exponent n
    bl printf

    @ Initialize computation with x and n
    ldr r0, =store_x           @ Reload x for calculations
    vldr s2, [r0]
    ldr r1, =store_n
    ldr r4, [r1]               @ Load n into r4 as counter

    vmov.f32 s3, #1.0          @ Initialize result to 1 in s3
    cmp r4, #0                 @ Check if exponent is zero
    beq display_result         @ If zero, skip to result display

calc_power:
    vmul.f32 s4, s3, s2        @ Multiply result by x
    vmov.f32 s3, s4            @ Store updated result
    subs r4, #1                @ Decrement n counter
    bne calc_power             @ Continue until n reaches 0

display_result:
    vcvt.f64.f32 d3, s3        @ Convert result to double for display
    ldr r0, =fmt_result_output
    vmov r1, r2, d3
    bl printf

finish:
    POP {PC}
    MOV PC, LR                 @ Return from function

.data
store_x:   .word 0                       @ Memory for x (float)
store_n:   .word 0                       @ Memory for n (integer)
msg_input_x: .asciz "Calculate x^n. Enter x: "    @ Prompt for x
msg_input_n: .asciz "Enter n: "                   @ Prompt for n
fmt_result_output: .asciz " = %f\n"               @ Output for result
fmt_exp_display: .asciz "^%d"                     @ Display for exponent
fmt_int_input: .asciz "%d"                        @ Input format for integer n
fmt_float_input: .asciz "%f"                      @ Input format for float x
fmt_float_display: .asciz "%f"                    @ Display format for x
