#include <stdio.h>
#include <stdlib.h>
#include<math.h>
#include<string.h>
struct Operation{
    unsigned char op: 3;
    unsigned char arg1: 2;
    unsigned char arg2: 2;

};

struct Instruction{
    struct Operation o;
    unsigned char v1;
    unsigned char v2;
};
// ---------------------------------

//Function 

struct Info{
    unsigned char label: 3;
    unsigned char nums: 5;
};

struct Func{
    struct Instruction *oplist;
    struct Info info;
};


struct Type{
    unsigned char name: 5;
    unsigned char type: 3;
};


struct Val{
    unsigned char value; //value
    struct Type info; //check name and type
};

struct Reg{
    unsigned char value; //store location
    unsigned char type; // check if address or value
};

// unsigned char find_pointer_value(struct Val *ram, unsigned char index);

// void  set_pointer_value(struct Val *ram, unsigned char index, unsigned char value, unsigned char type);

// void freeAll(struct Func **list);

// int execute(struct Reg *r, struct Val *ram, struct Func **func_list);

// int readFile(char **argv, struct Func **func_list);





