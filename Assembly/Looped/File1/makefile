#Program name

OBJS = 1_loop_ex4_1.o

DEBUG = 1

ifdef DEBUG
DEBUGFLGS = -g

else
DEBUGFLGS =
endif

# The % is a wildcard.  For below, reads as for all .s files and create a .0 file with DEBUGFLGS output
%.o : %.s
	as $(DEBUGFLGS) $< -o $@
1_loop_ex4_1: $(OBJS)
	ld -o 1_loop_ex4_1 $(OBJS)


