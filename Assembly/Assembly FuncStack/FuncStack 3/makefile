#Program name

OBJS = FuncStack3_ex6_18.o

DEBUG = 1

ifdef DEBUG
DEBUGFLGS = -g

else
DEBUGFLGS =
endif

# The % is a wildcard.  For below, reads as for all .s files and create a .0 file with DEBUGFLGS output
%.o : %.s
	as $(DEBUGFLGS) $< -o $@
FuncStack3_ex6_18: $(OBJS)
	ld -o FuncStack3_ex6_18 $(OBJS)


