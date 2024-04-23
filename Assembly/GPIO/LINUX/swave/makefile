OBJS = Linux_asm_squarewave.o
ifdef DEBUG
DEBUGFLGS = -g
else
DEBUGFLGS =
endif

%.o : %.s
	as $(DEBUGFLGS) $< -o $@
Linux_asm_squarewave: $(OBJS)
	gcc -o Linux_asm_squarewave  $(OBJS)

clean:
	rm *.o Linux_asm_squarewave
