#include <stdio.h>
#include <stdlib.h>
#include<math.h>
#include<string.h>


// Instruction

struct Operation{
    unsigned char op: 3;
    unsigned char arg1: 2; 
    unsigned char arg2: 2;

};

struct Instruction{ //   
    struct Operation o;
    unsigned char v1;
    unsigned char v2;
};
// ---------------------------------

//Function 

struct Info{
    unsigned char label: 3; //function label
    unsigned char nums: 5; //nums of instructions
};

struct Func{
    struct Instruction *oplist; //op codes
    struct Info info;
};


struct Type{
    unsigned char name: 5;  //symbol name
    unsigned char type: 3; //check if address or value
};


struct Val{
    unsigned char value; //value
    struct Type info; //check name and type
};

struct Reg{
    unsigned char value; //store location
    unsigned char type; // check if address or value
};



/*my idea is , I use any array[128] as a stack which store the Vals . then I use the register 4 to store 

the previous instruction address(in value) and the previous stack frame location , use register 5 to store the the end of current

frame location and use 6 as the stack frame pointer */


unsigned char find_pointer_value(struct Val *ram, unsigned char index){

    
    unsigned char val = index; //just for good looking and easy understanding

    while(ram[val].info.type != 0){

        val = ram[val].value;  //it means that here the value is address type and program will continue to find the next one

    }

   
    return ram[val].value; //find the value 
    
}

void  set_pointer_value(struct Val *ram, unsigned char index, unsigned char value, unsigned char type){
    
    unsigned char val = index;

    while(ram[val].info.type != 0){

        val = ram[val].value;

    }

    ram[val].value = value;

    ram[val].info.type = type; //type is checking whether it is address or value

    
}

unsigned char find_pointer_index(struct Val *ram, unsigned char index){

    
    unsigned char val = index;

    while(ram[val].info.type != 0){

        val = ram[val].value;

    }

    
    return val;
    
}






unsigned char check(struct Val *ram, struct Reg *r, unsigned char symbol){

    unsigned char end = r[5].value;

    unsigned char ptr = r[6].value; //for understanding



    

    while(ptr < end){

        
        if(ram[ptr].info.name == symbol + 1){

            
            
             return ptr; // check whether the symbol name in the current frame are same as "symbol"
        }
        ptr = ptr + 1;
    }

    return r[4].value;
}


int update(struct Val *ram, struct Reg *r){
    
    /*clean the data*/
    ram[r[5].value].value = 0; 
    
    ram[r[5].value].info.name = 0;
    
    ram[r[5].value].info.type = 0;
    
    r[5].value++; //when updating the symbol, the num of the end of the stack frame should increase 1
    
    if(r[5].value > 127){
        
        return 1; //prevent stack from stackoverflow
    
    }else{
        
        return 0;
    }

    
}






int MOV(struct Instruction *current, struct Reg *r, struct Val *ram){

    unsigned char value;
    
    unsigned char type;

    if(current->o.arg2 == 0){ //arg2 means argument 2
       
        value = current->v2;
        
        type = 0; 
        
        
        
    }
    else if(current->o.arg2 == 1){
        
        value = r[current->v2].value; //register value
        
        type = r[current->v2].type; //register type (only for 0 - 3)

       
        
    }

    else if(current->o.arg2 == 2){
        
        unsigned char index = check(ram, r, current->v2);
        
        if(index == r[4].value){
            
           return 1;
                    
        }else{

        
            
            value = ram[index].value;
            
            type = ram[index].info.type;


        }
        
    }
    else if(current->o.arg2 == 3){
        
        unsigned char index = check(ram, r, current->v2);
        
        if(index == r[4].value){
           
           return 1;
                    
        }else{
           


        value = find_pointer_value(ram, index);
        
        type = 0;

            

        }
    }else{
        printf("cannot get here \n");
        
        return 1;
    }

    
    //check arg1
    if(current->o.arg1 == 0){
        
        return -1;
    }
    else if(current->o.arg1 == 1){
        
        r[current->v1].value = value;

        if(type == 0){
            
            r[current->v1].type = 0;
        
        }else{
            
            r[current->v1].type = 1;
        }
        //printf("move to reg: %d type: %d\n", value,type );
    }

    else if(current->o.arg1 == 2){
        
        
        unsigned char index = check(ram, r, current->v1);
        
        if(index == r[4].value){

            if(update(ram, r) == 1){
                
                return 1;
            
            }else{
                
                index = r[5].value - 1;

                ram[index].value = value;
                
                ram[index].info.name = current->v1 + 1;

                if(type == 0){
                    
                    ram[index].info.type = 0;
                
                }else{
                    
                    ram[index].info.type = 1;
                }

                

               //printf("move to stak value %d name %d type %d\n", ram[index].value, ram[index].info.name, ram[index].info.type);
            }
                    
        }else{
                ram[index].value = value;
                
                ram[index].info.name = current->v1 + 1;

                if(type == 0){
                    
                    ram[index].info.type = 0;
                
                }else{
                    
                    ram[index].info.type = 1;
                }

                
            
        }
    }
    else if(current->o.arg1 == 3){
        
        unsigned char index = check(ram, r, current->v1);

        
        if(index == r[4].value){
            
            if(update(ram, r) == 1){
                
                return 1;
            
            }else{
                index = r[5].value - 1;
                

                set_pointer_value(ram, index, value, type);


            }
                    
        }else{
            
           
            set_pointer_value(ram, index, value, type);
        }
    }else{
        
        printf("cannot get here \n");
        
        return 1;
    }

    
    
    return 0;



}


int CAL(struct Val *ram, struct Reg *r, unsigned char v){
    
    if(r[5].value + 1 > 127){
        //prevent from stack overflow
        return 1;
    }
    
    /*store the previous instruction*/
    ram[r[5].value].info.name = r[7].value &  0x1F; 
    
    ram[r[5].value].info.type = r[7].value >> 5 & 0x07;

    /*----*/


    /*store the start location of previous frame */
    ram[r[5].value].value = r[4].value;

    /**/


    /*set the new current frame*/
    r[4].value = r[5].value;

    r[5].value++;

    r[6].value = r[5].value;
    /*-------------*/

    /*jump to another function*/
    r[7].value = v;

    
    return 0;
  
}

void RET(struct Val *ram, struct Reg *r){

    r[6].value = r[4].value + 1;
    
    /*clean all data in the current frame*/
   
    while(r[6].value < r[5].value){
        
        ram[r[6].value].value = 0;
        
        ram[r[6].value].info.name = 0;
        
        ram[r[6].value].info.type = 0;     
        
        r[6].value++;

    }
    
    ram[r[5].value].info.name = 0;
    
    ram[r[5].value].info.type = 0;
    
    ram[r[5].value].value = 0;

    /*-----------------------------------*/

    /*go back to previous stack frame*/
    
    r[5].value = r[4].value;
    
    r[4].value = ram[r[5].value].value;
    
    if(r[4].value == r[5].value && r[4].value == 0){
        
        r[6].value = r[4].value;
    
    }else{
       
       r[6].value = r[4].value + 1; 
    }

    /*jump back */
    r[7].value = ram[r[5].value].info.type << 5 | ram[r[5].value].info.name;


    
}



int REF(struct Instruction *current, struct Reg *r, struct Val *ram){

    unsigned char res;

    if(current->o.arg2 == 0){
        
        return 1;
    }
    
    else if(current->o.arg2 == 1){
        
        return 1;
    }
    
    else if(current->o.arg2 == 2){
        
        unsigned char index = check(ram, r, current->v2);

        
        if(index == r[4].value){

            return 1; //cannot find the symbol
        
        }else{
            
            res = index;
            
        }
                
    }else if(current->o.arg2 == 3){
        
        unsigned char index = check(ram, r, current->v2);
        
        if(index == r[4].value){
        

            return 1; 
        }else{
            

           

            res = find_pointer_index(ram, index);
        }
                
    }else{
        
        return 1;
    }


    if(current->o.arg1 == 0){
        
        return 1;
    }
    else if(current->o.arg1 == 1){
        
        r[current->v1].value = res;
        
        r[current->v1].type = 1;
    }
    else if(current->o.arg1 == 2){
        
        unsigned char index = check(ram, r, current->v1);
        
        if(index == r[4].value){
            
            if(update(ram, r) == 1){
                
                return 1;
            
            }else{
                
                index = r[5].value - 1;
                
                ram[index].value = res;
                
                ram[index].info.name = current->v1 + 1;
                
                ram[index].info.type = 1;
               
                }
                    
        }else{
            ram[index].value = res;
            
            ram[index].info.name = current->v1 + 1;
            
            ram[index].info.type = 1;
            
         
        }
    }
    else if(current->o.arg1 == 3){
        
        unsigned char index = check(ram, r, current->v1);
        
        if(index == r[4].value){
            
            

            if(update(ram, r) == 1){
                
                return 1;
            
            }else{

                index = r[5].value - 1;

                set_pointer_value(ram, index, res, 1);
                
                }
                    
        }else{
            
            
            set_pointer_value(ram, index, res, 1);

        }

    }else{
        printf("cannot reach here\n");
        return 1;
    }
    

    return 0;

}



void ADD(struct Reg *r, unsigned char v1, unsigned char v2){
     
    r[v1].value = r[v1].value + r[v2].value;
    
 
}



int PRI(struct Reg *r, struct Val *ram, struct Instruction *current){

    if(current->o.arg1 == 0){
       
        printf("%d\n", current->v1);
    
    }
    else if(current->o.arg1 == 1){

        printf("%d\n", r[current->v1].value);
    
    }

    else if(current->o.arg1 == 2){
        
        unsigned char index = check(ram, r, current->v1);
        
        if(index == r[4].value){
            
            printf("no this symbol");
            
            return 1;
                    
        }else{
            
            printf("%d\n", ram[index].value);
        }
        
    }else if(current->o.arg1 == 3){
        
        unsigned char index = check(ram, r, current->v1);
        
        if(index == r[4].value){

            return 1;
                    
        }else{
            
            unsigned char res = find_pointer_value(ram, index);
            
            printf("%d\n", res);
        }
        
    }
    return 0;
}


void NOT(struct Reg *r, unsigned char v){
    
    (r[v].value) = ~((r[v].value));

}


void EQU(struct Reg *r, unsigned char v){

    if((r[v].value) == 0){
        
        (r[v].value) = 1;
    
    }else{
        
        (r[v].value) = 0;
    }

}

//--------------------------------------------------



int execute(struct Reg *r, struct Val *ram, struct Func **func_list)
{       
        //get the current instruction by the program counter
        struct Instruction *current = &func_list[(r[7].value) >> 5 & 0x07]->oplist[(r[7].value)& 0x1F];

       

        r[7].value++;

        
        
        if(current->o.op == 0){
            
            if(MOV(current, r, ram) == 1){
                
                return 1; //fail
            
            }else{
                
                return 0;
            }
        }
        else if(current->o.op == 1){
            
            unsigned char nextIns;

            nextIns = (current->v1) << 5;

        

            if(CAL(ram, r, nextIns) == 1){ 
                
                return 1;

            }else{
                
                return 0;

            }
        }
        else if(current->o.op == 2){
            
            RET(ram, r);
            
            return 0;
        }
        else if(current->o.op == 3){
            
            if(REF(current, r, ram) == 1){
                
                return 1;
            
            }else{
                
                return 0;
            }
        }
        else if(current->o.op == 4){
            
            if(current->o.arg1 != 1 || current->o.arg2 != 1){
                
                return 1;
            
            }else{
                
                ADD(r, current->v1, current->v2);
            }
        }
        else if(current->o.op == 5){
            
            if(PRI(r, ram, current) == 1){
                
                return 1;
            }
        }
        
        else if(current->o.op == 6){
            
            if(current->o.arg1 != 1){
                   
                   return 1;
                
                }else{
                    
                    NOT(r, current->v1);
                }
        }
        else if(current->o.op == 7){
            
            if(current->o.arg1 != 1){
                   
                   return 1;
                
                }else{
                    
                    EQU(r, current->v1);
                }
        }
        else{
            
            printf("cannot get here\n");
            return 1;
        }
        return 0;


}

int parse(unsigned char *x, unsigned char *y, char num, FILE *fp){


     unsigned char bits = pow(2, num) - 1;

    if(*x <= num && *y > 0){
        
        unsigned char hex1 = 0, *b1 = &hex1;
        
        fseek(fp, *y , SEEK_SET);
        
        fread(b1, 1, 1, fp);
        
        *y = *y - 1;
        
        unsigned char hex2 = 0, *b2 = &hex2;
        
        fseek(fp, *y , SEEK_SET);
        
        fread(b2, 1, 1, fp);  
        
        int res = (*b1 >> (8 - *x) | *b2 << *x) & bits;
        
        *x = *x + 8 - num;


        return res;
        
    }else if(*x > num && *y >= 0){
        
        unsigned char hex = 0, *b = &hex;
        
        fseek(fp, *y , SEEK_SET);
        
        fread(b, 1, 1, fp);
        
        int res = ( *b >> (8 - *x)) & bits; 
        
        *x = *x - num;      
        
        return res;
    
    }else{
        // handle error: there is no line to parse
        return -1;
    }
    
}


int makeFunc(unsigned char* x, unsigned char* y, FILE* fp, struct Func *func){


    int res = parse(x, y, 5, fp);
    

    if(res < 0){
        
        return -1; //line limit
    } 

    

    func->info.nums = res & 0x1F;

    func->oplist = malloc(sizeof(struct Instruction) * (func->info.nums));

    
    if(func->oplist == NULL){
        
        return -3; // no much value for a instruction list
    }
    
    for(int j = (func->info.nums) - 1; j >= 0; j--){
        
        int op = parse(x, y, 3, fp);

         
        if(op == 0x02){

            func->oplist[j].o.op= op;

            continue;


      }else if(op == 0x01 || op == 0x05 || op == 0x06 || op == 0x07){
            // check first value
            int t1 = parse(x,y, 2, fp);

            
           
            if(t1 == -1){
                
                return -2;
            
            }else if(t1 == 0){
                
                int v1 = parse(x, y, 8, fp);
               
                if(v1 == -1){
                
                return -2;
                }
                
                func->oplist[j].v1 = v1;
                
                func->oplist[j].o.arg1 = t1;
                
                func->oplist[j].o.op = op;

            }else if (t1 == 1){
                
                int v1 = parse(x, y, 3, fp);
                
                if(v1 == -1){
                
                return -2;
                }
                func->oplist[j].v1 = v1;
                
                func->oplist[j].o.arg1 = t1;
                
                func->oplist[j].o.op = op;
            
            }else if(t1 == 2){
                
                int v1 = parse(x, y, 5, fp);
                
                if(v1 == -1){
                
                return -2;
                
                }
                func->oplist[j].v1 = v1;
                
                func->oplist[j].o.arg1 = t1;
                
                func->oplist[j].o.op = op;

            }else if(t1 == 3){
                
                int v1 = parse(x, y, 5, fp);
               
                if(v1 == -1){
                
                return -2;
                }
                
                func->oplist[j].v1 = v1;
                
                func->oplist[j].o.arg1 = t1;
                
                func->oplist[j].o.op = op;

            }else{
                //error
            }
        

        }else if (op == 0x00 || op == 0x03 || op == 0x04){
            
            int t1 = parse(x,y, 2, fp);
       
            if(t1 == -1){
                
                return -2;
            
            }else if(t1 == 0){
                
                int v1 = parse(x, y, 8, fp);
                
                if(v1 == -1){
                
                return -2;
                }
                func->oplist[j].v1 = v1;
                
                func->oplist[j].o.arg1 = t1;
                
                func->oplist[j].o.op = op;

            }else if (t1 == 1){
                
                int v1 = parse(x, y, 3, fp);
                
                if(v1 == -1){
                
                return -2;
                }
                
                func->oplist[j].v1 = v1;
                
                func->oplist[j].o.arg1 = t1;
                
                func->oplist[j].o.op = op;
            
            }else if(t1 == 2){
                
                int v1 = parse(x, y, 5, fp);
                
                if(v1 == -1){
                
                return -2;
                }
                
                func->oplist[j].v1 = v1;
                
                func->oplist[j].o.arg1 = t1;
                
                func->oplist[j].o.op = op;

            }else if(t1 == 3){
                
                int v1 = parse(x, y, 5, fp);
                
                if(v1 == -1){
                
                return -2;
                }
                
                func->oplist[j].v1 = v1;
                
                func->oplist[j].o.arg1 = t1;
                
                func->oplist[j].o.op = op;

            }else{
                //error
            }

               
            int t2 = parse(x,y, 2, fp);

           
            if(t2 == -1){
                
                return -2;
            
            }else if(t2 == 0){
                
                int v2 = parse(x, y, 8, fp);
                
                if(v2 == -1){
                
                return -2;
                }
                
                func->oplist[j].v2 = v2;
                
                func->oplist[j].o.arg2 = t2;
                
                func->oplist[j].o.op = op;

            }else if (t2 == 1){
                
                int v2 = parse(x, y, 3, fp);
                
                if(v2 == -1){
                
                return -2;
                }
                
                func->oplist[j].v2 = v2;
                
                func->oplist[j].o.arg2 = t2;
                
                func->oplist[j].o.op = op;
            }else if(t2 == 2){
                
                int v2 = parse(x, y, 5, fp);
                
                if(v2 == -1){
                
                return -2;
                }
                
                func->oplist[j].v2 = v2;
                
                func->oplist[j].o.arg2 = t2;
                
                func->oplist[j].o.op = op;

            }else if(t2 == 3){
                
                int v2 = parse(x, y, 5, fp);
                
                if(v2 == -1){
                
                return -2;
                }
                
                func->oplist[j].v2 = v2;
                
                func->oplist[j].o.arg2 = t2;
                
                func->oplist[j].o.op = op;

            }else{
                //error
            }
        
            

        }else{
            return -2;
        }

    }

    int lab = parse(x,y,3,fp);
    
    if(lab < 0){
        
        return -2;
    }

    (func->info).label = lab & 0x7;

    return 0;

        
}



void freeAll(struct Func **list){
    
    for(int i = 0; i < 8; i++){
        
        if(list[i] != NULL){
        
        free(list[i]->oplist);
        
        list[i]->oplist = NULL;
        
        free(list[i]);
        
        list[i] = NULL;
        }
        
    }
    free(list);
}


int readFile(char **argv, struct Func **func_list){
    FILE *fp;
   /* Open file for reading binary data*/
   fp = fopen(argv[1], "rb");
   
   if(fp == NULL){
       
       printf("cannot open the file.\n");
       
       return 1;
   }

   else if(fseek(fp, 0, SEEK_END) != 0){
       
       printf("something goes wrong in the file\n");
       
       fclose(fp);
       
       return 1;
       
   }
   else if(ftell(fp) <= 0){
       
       printf("file is empty\n");
       
       fclose(fp);
       
       return 1;
       
   }else{
       //keep the position of the file
        unsigned char xVal = 8, *x = &xVal;
        
        unsigned char yVal = ftell(fp) - 1, *y = &yVal;

       

        int i = 0; //error type
        
        int j = 0;

       

        while(1){

    
        
            if(j >= 8){
                return 1;
            }
        

            struct Func *newfunc = malloc(sizeof(struct Func));
            
            if(newfunc == NULL){
                return 1;
                break;
            
            }   

            //check if function is ok
            i = makeFunc(x,y,fp, newfunc);

            
        
            if(i == 0){ 

           
                
                func_list[newfunc->info.label] = malloc(sizeof(struct Func));
                
                memcpy(func_list[newfunc->info.label], newfunc, sizeof(struct Func));
                
                free(newfunc);
                
                newfunc = NULL;
                
                j++;
                
                continue;

            }else if(i == -1){
                
                free(newfunc);
                
                newfunc = NULL;
                
                break;
        
            }else if(i == -2){
                free(newfunc->oplist);
                
                free(newfunc);
                
                newfunc = NULL;
                
                break;
       
            }else if(i == -3){
                
                free(newfunc);
                
                newfunc = NULL;
                
                break;
            }else{
                break;
            }

        }
    fclose(fp);
    
    return 0;
    }
   
}
