#Program name

OBJS = 2_loop_Prog4_1.o

DEBUG = 1

ifdef DEBUG
DEBUGFLGS = -g

else
DEBUGFLGS =
endif

# The % is a wildcard.  For below, reads as for all .s files and create a .0 file with DEBUGFLGS output
%.o : %.s
	as $(DEBUGFLGS) $< -o $@
2_loop_Prog4_1: $(OBJS)
	ld -o 2_loop_Prog4_1 $(OBJS)

#cleanup
clean: $(OBJS)
	rm *.o 2_loop_Prog4_1
