

OBJS =indirect.o

DEBUG = 1

ifdef DEBUG
DEBUGFLGS = -g

else
DEBUGFLGS =
endif

# The % is a wildcard.  For below, reads as for all .s files and create a .0 file with DEBUGFLGS output
%.o : %.s
	as $(DEBUGFLGS) $< -o $@
indirect: $(OBJS)
	ld -o indirect $(OBJS)

#cleanup
clean: $(OBJS)
	rm *.o indirect
