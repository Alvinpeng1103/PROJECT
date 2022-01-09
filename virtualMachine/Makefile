CC=gcc
CFLAGS=-fsanitize=address -Wvla -Wall -Werror -g -std=gnu11 -lm -lasan


# fill in all your make rules

vm_x2017: vm_x2017.c
	${CC} ${CFLAGS} $^ -o $@

objdump_x2017: objdump_x2017.c
	${CC} ${CFLAGS} $^ -o $@

testVM: vm_x2017.c
	make vm_x2017
	

test: test.sh
	bash ./test.sh
	




clean:
	rm vm_x2017
	rm objdump_x2017




	
