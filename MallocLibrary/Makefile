CC=gcc
CFLAGS=-fsanitize=address -Wall -Werror -std=gnu11 -g -lm -Wno-deprecated-declarations

tests: tests.c virtual_alloc.c
	$(CC) $(CFLAGS) $^ -o $@


run_tests: test.sh

	./tests
	bash ./test.sh

