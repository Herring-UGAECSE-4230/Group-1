
@ mmap part taken from by https://bob.cs.sonoma.edu/IntroCompOrg-RPi/sec-gpio-mem.html

@ Constants for blink at GPIO21
@ GPFSEL1 [Offset: 0x04] responsible for GPIO Pins 13 to 19
@ GPCLR0 [Offset: 0x28] responsible for GPIO Pins 0 to 31
@ GPSET0 [Offest: 0x1C] responsible for GPIO Pins 0 to 31

@ GPOI17 Related
.equ    GPFSEL1, 0x04   @ function register offset
.equ    GPCLR0, 0x28    @ clear register offset
.equ    GPSET0, 0x1c    @ set register offset
.equ    GPFSEL1_GPIO17_MASK, 0b111000000000000000000000   @ Mask for fn register
.equ    MAKE_GPIO17_OUTPUT, 0b1000000000000000000000      @ use pin for ouput
.equ    PIN, 17                         @ Used to set PIN high / low

@ Args for mmap
.equ    OFFSET_FILE_DESCRP, 0   @ file descriptor
.equ    mem_fd_open, 3
.equ    BLOCK_SIZE, 4096        @ Raspbian memory page
.equ    ADDRESS_ARG, 3          @ device address

@ Misc
.equ    SLEEP_IN_S,1            @ sleep one second
.equ    ON_DELAY, 10000    @  On Delay time in nanoseconds
.equ    OFF_DELAY,990000   @  Off Delay time in nanoseconds

@ The following are defined in /usr/include/asm-generic/mman-common.h:
.equ    MAP_SHARED,1    @ share changes with other processes
.equ    PROT_RDWR,0x3   @ PROT_READ(0x1)|PROT_WRITE(0x2)

@ Constant program data
    .section .rodata
device:
    .asciz  "/dev/gpiomem"


@ The program
    .text
    .global main
main:

@ Open /dev/gpiomem for read/write and syncing
    ldr     r1, O_RDWR_O_SYNC   @ flags for accessing device
    ldr     r0, mem_fd          @ address of /dev/gpiomem
    bl      open     
    mov     r4, r0              @ use r4 for file descriptor

@ Map the GPIO registers to a main memory location so we can access them
@ mmap(addr[r0], length[r1], protection[r2], flags[r3], fd[r4])
    str     r4, [sp, #OFFSET_FILE_DESCRP]   @ r4=/dev/gpiomem file descriptor
    mov     r1, #BLOCK_SIZE                 @ r1=get 1 page of memory
    mov     r2, #PROT_RDWR                  @ r2=read/write this memory
    mov     r3, #MAP_SHARED                 @ r3=share with other processes
    mov     r0, #mem_fd_open                @ address of /dev/gpiomem
    ldr     r0, GPIO_BASE                   @ address of GPIO
    str     r0, [sp, #ADDRESS_ARG]          @ r0=location of GPIO
    bl      mmap
    mov     r5, r0           @ save the virtual memory address in r5

@ Set up the GPIO pin funtion register in programming memory
    add     r0, r5, #GPFSEL1            @ calculate address for GPFSEL1
    ldr     r2, [r0]                    @ get entire GPFSEL1 register
    bic     r2, r2, #GPFSEL1_GPIO17_MASK@ clear pin field
    orr     r2, r2, #MAKE_GPIO17_OUTPUT @ enter function code
    str     r2, [r0]                    @ update register

    PUSH {r3,r5}
@the code below calculates a tenth of ON and OFF delay and subtracts this from ON and OFF delay
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
	blt continue
	add r6, r6, #1
	b inner2 

 # these are instructions to increment r5 or r6 once more if subtracting r4 from r3 yields a 0
extra1:
	add r5, r5, #1
	b calc2
extra2: 
	add r6, r6, #1
	b continue
 @this code subtracts the tenth from ON_DELAY and OFF_DELAY and stores each in r4 and r6 respectively
 continue:
 ldr r1, =ON_DELAY
 sub r4, r1,r5
 ldr r1, =OFF_DELAY
 sub r6, r1, r6
    
POP{r3,r5}
loop:

@ Turn on
    add     r0, r5, #GPSET0 @ calc GPSET0 address

    mov     r3, #1          @ turn on bit
    lsl     r3, r3, #PIN    @ shift bit to pin position
    orr     r2, r2, r3      @ set bit
    str     r2, [r0]        @ update register
    PUSH {r0}

    bl delay1
    
   POP {r0}
@ Turn off
   add     r0, r5, #GPCLR0  @Calculate GPCLR0 address
   lsl     r3, r3, #PIN
   orr     r2, r2, r3
   str     r2, [r0]
  PUSH {r0}

  bl delay2

  POP {r0}
   
  b loop

delay1:
  mov r0, r4
lp1:
  subs r0,#1
  bne lp1
  bx lr


delay2:
  mov r0, r6
lp2:
  subs r0,#1
  bne lp2
  bx lr





GPIO_BASE:
    .word   0xfe200000  @GPIO Base address Raspberry pi 4
mem_fd:
    .word   device
O_RDWR_O_SYNC:
    .word   2|256       @ O_RDWR (2)|O_SYNC (256).
