
.include "unistd.s"
.include "classinclude.s"

.global _start

_start:
	MOV R1, #0x14
	ADD R0, R1, #0XA
	MOV R7, #sys_exit
	SWI sys_restart_syscall

