#Program name

OBJS = FuncStack2_Prog4_3.o

DEBUG = 1

ifdef DEBUG
DEBUGFLGS = -g

else
DEBUGFLGS =
endif

# The % is a wildcard.  For below, reads as for all .s files and create a .0 file with DEBUGFLGS output
%.o : %.s
	as $(DEBUGFLGS) $< -o $@
FuncStack2_Prog4_3: $(OBJS)
	ld -o FuncStack2_Prog4_3 $(OBJS)


