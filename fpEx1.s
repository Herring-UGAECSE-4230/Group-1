    .text
    .global _start
    .extern printf           @ Declare printf as an external function

_start:
    vmov.f32    s0, #0.125          @ Set radius to 0.125 (change this for different values)
    vmul.f32    s0, s0, s0          @ s0 = radius^2
    ldr         r2, =piNumber
    vldr        s1, [r2]            @ Load pi into s1
    vmul.f32    s0, s0, s1          @ s0 = pi * radius^2

    vcvt.f64.f32 d0, s0             @ Convert single-precision float to double-precision
                                    @ (since printf expects doubles for %f format)

    @ Move the result into x0 and prepare arguments for printf
    ldr         x0, =fmtString      @ Load address of format string into x0
    fmov        d0, s0              @ Move the double result from d0 to use as an argument
    mov         x1, d0              @ Move the result into x1 for printf's %f

    bl          printf              @ Call printf function

    @ Exit program
    mov         x8, #93             @ syscall number for exit on aarch64
    mov         x0, #0              @ exit code 0
    svc         #0

.data
fmtString: .asciz "The area of the circle is: %f\n"  @ Format string for printf
piNumber: .float 3.141593