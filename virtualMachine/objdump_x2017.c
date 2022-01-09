#include <stdio.h>
#include <stdlib.h>
#include <math.h>



struct Instruct{
    unsigned char opcode;
    unsigned char value[2];
    unsigned char arg[2];
};

struct Info{
    unsigned char label: 3;
    unsigned char nums: 5;
};

struct Func{
    struct Info info;
    struct Instruct *oplist;
};








 int parse(unsigned char *x, unsigned char *y, char num, FILE *fp){


     unsigned char bits = pow(2, num) - 1;

    //cross line section

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
        

        //does not cross line
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


   

    
    

    func->oplist = malloc(sizeof(struct Instruct) * res); 

    if(func->oplist == NULL){
        
        return -3; // no much value for a instruction list
    }

   


    for(int j = 0; j < res; j++){
        
        int op = parse(x, y, 3, fp);
         

        if(op == 0x02){


            func->oplist[j].opcode = op;
            
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
                
                func->oplist[j].value[0] = v1;
                
                func->oplist[j].arg[0] = t1;
                
                func->oplist[j].opcode = op;

            }else if (t1 == 1){
                int v1 = parse(x, y, 3, fp);
                
                if(v1 == -1){
                
                return -2;
                }
                func->oplist[j].value[0] = v1;
                
                func->oplist[j].arg[0] = t1;
                
                func->oplist[j].opcode = op;
            
            }else if(t1 == 2){
                
                int v1 = parse(x, y, 5, fp);
                
                if(v1 == -1){
                
                return -2;
                }
                func->oplist[j].value[0] = v1;
                
                func->oplist[j].arg[0] = t1;
                
                func->oplist[j].opcode = op;

            }else if(t1 == 3){
                
                int v1 = parse(x, y, 5, fp);
               
                if(v1 == -1){
                
                return -2;
                }
                func->oplist[j].value[0] = v1;
                
                func->oplist[j].arg[0] = t1;
                
                func->oplist[j].opcode = op;

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
                func->oplist[j].value[0] = v1;
                func->oplist[j].arg[0] = t1;
                func->oplist[j].opcode = op;

            }else if (t1 == 1){
                int v1 = parse(x, y, 3, fp);
                if(v1 == -1){
                return -2;
                }
                func->oplist[j].value[0] = v1;
                func->oplist[j].arg[0] = t1;
                func->oplist[j].opcode = op;
            }else if(t1 == 2){
                int v1 = parse(x, y, 5, fp);
                if(v1 == -1){
                return -2;
                }
                func->oplist[j].value[0] = v1;
                func->oplist[j].arg[0] = t1;
                func->oplist[j].opcode = op;

            }else if(t1 == 3){
                int v1 = parse(x, y, 5, fp);
                if(v1 == -1){
                return -2;
                }
                func->oplist[j].value[0] = v1;
                func->oplist[j].arg[0] = t1;
                func->oplist[j].opcode = op;

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
                func->oplist[j].value[1] = v2;
                func->oplist[j].arg[1] = t2;
                func->oplist[j].opcode = op;

            }else if (t2 == 1){
                int v2 = parse(x, y, 3, fp);
                if(v2 == -1){
                return -2;
                }
                func->oplist[j].value[1] = v2;
                func->oplist[j].arg[1] = t2;
                func->oplist[j].opcode = op;
            }else if(t2 == 2){
                int v2 = parse(x, y, 5, fp);
                if(v2 == -1){
                return -2;
                }
                func->oplist[j].value[1] = v2;
                func->oplist[j].arg[1] = t2;
                func->oplist[j].opcode = op;

            }else if(t2 == 3){
                int v2 = parse(x, y, 5, fp);
                if(v2 == -1){
                return -2;
                }
                func->oplist[j].value[1] = v2;
                func->oplist[j].arg[1] = t2;
                func->oplist[j].opcode = op;

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




   
void funcPrint(struct Func f){

    
    unsigned char symbols[32] = {0};
    
    unsigned char symbol_num = 1;
    
    int i = f.info.nums - 1;

    char t[4][4] = {"VAL", "REG", "STK", "PTR"};
    
    char o[8][6] = {"MOV", "CAL", "RET", "REF", "ADD", "PRINT", "NOT", "EQU"};

    printf("FUNC LABEL %d\n", f.info.label);

   
    while(i >= 0){
        
        int op = f.oplist[i].opcode;

        if(op == 0x02){
            printf("    RET\n");

        }
        else if(op == 0x01 || op == 0x05 || op == 0x06 || op == 0x07){
            
            int type1 = (f.oplist)[i].arg[0];
            
            int v1 = (f.oplist)[i].value[0];

            unsigned char symbol1;
            
            if(type1 == 2 || type1 == 3){
                
                
                if(symbols[v1] != 0){
                    
                    if(symbols[v1] <= 26){
                       
                       symbol1 = symbols[v1] + 64; 
                    
                    }else{
                        
                        symbol1 = symbols[v1] + 64 + 6;
                    }
                    
                }else{
                    
                    symbols[v1] = symbol_num;
                    
                    symbol1 = symbols[v1];
                    
                    if(symbol1 <= 26){
                        
                        symbol1 = symbol1 + 64;
                    
                    }else{
                        
                        symbol1 = symbol1 + 64 + 6;
                    }
                    
                    symbol_num++;
                    
                }
                
                printf("    %s %s %c\n" ,o[op], t[type1], symbol1);

            }else{
                
                printf("    %s %s %d\n" ,o[op], t[type1], v1);
            }
                     

        }else if( op == 0x00 || op == 0x03 || op == 0x04){
            
            int type1 = (f.oplist)[i].arg[0];
            
            int v1 = (f.oplist)[i].value[0];
            
            int type2 = (f.oplist)[i].arg[1];
            
            int v2 = (f.oplist)[i].value[1];

            
        

            if(type1 == 2 || type1 == 3){

                unsigned char symbol1;
                
                if(symbols[v1] != 0){
                    
                    if(symbols[v1] <= 26){
                       
                       symbol1 = symbols[v1] + 64; 
                    
                    }else{
                        
                        symbol1 = symbols[v1] + 64 + 6;
                    }
                    
                }else{
                    
                    symbols[v1] = symbol_num;
                    
                    symbol1 = symbols[v1];
                    
                    if(symbol1 <= 26){
                        
                        symbol1 = symbol1 + 64;
                    
                    }else{
                        
                        symbol1 = symbol1 + 64 + 6;
                    }
                    
                    symbol_num++;
                    
                }

            

                if(type2 == 2 || type2 == 3){
                
                    unsigned char symbol2;
                    
                    if(symbols[v2] != 0){
                        
                        if(symbols[v2] <= 26){
                            
                            symbol2 = symbols[v2] + 64; 
                        
                        }else{
                            
                            symbol2 = symbols[v2] + 64 + 6;
                        }
                    
                    }else{
                        
                        symbols[v2] = symbol_num;
                        
                        symbol2 = symbols[v2];
                        
                        if(symbol2 <= 26){
                            
                            symbol2 = symbol2 + 64;
                        
                        }else{
                            
                            symbol2 = symbol2 + 64 + 6;
                        }
                        
                        symbol_num++;
                        }
                    
                    printf("    %s %s %c %s %c\n" , o[op], t[type1], symbol1, t[type2] , symbol2);
                }         
                
                else{

                    printf("    %s %s %c %s %d\n" , o[op], t[type1], symbol1, t[type2] , v2);

                }

            }else{
        

                if(type2 == 2 || type2 == 3){
                
                unsigned char symbol2;
                
                
                if(symbols[v2] != 0){
                    
                    if(v2 <= 26){
                       
                       symbol2 = symbols[v2] + 64; 
                    
                    }else{
                        
                        symbol2 = symbols[v2] + 64 + 6;
                    }
                    
                }else{

                    symbols[v2] = symbol_num;
                        
                        symbol2 = symbols[v2];
                        
                        if(symbol2 <= 26){
                            
                            symbol2 = symbol2 + 64;
                        
                        }else{
                            
                            symbol2 = symbol2 + 64 + 6;
                        }
                        
                        symbol_num++;
                }
                
                printf("    %s %s %d %s %c\n" , o[op], t[type1], v1, t[type2] , symbol2);

                }else{

                    printf("    %s %s %d %s %d\n" , o[op], t[type1], v1, t[type2] , v2);

                }

            }

        }else{
            //handle error;
        }

        i--;

    }
    

}




int main(int argc, char *argv[]){
   FILE *fp;
   /* Open file for reading binary data*/
   fp = fopen(argv[1], "rb");
   
   if(fp == NULL){
       /* handle error */
   }

   if(fseek(fp, 0, SEEK_END) != 0){
       /* handle error */
   }

   if(ftell(fp) <= 0){
       /* handle error */
       // file is empty
   }

   unsigned char xVal = 8, *x = &xVal;
   unsigned char yVal = ftell(fp) - 1, *y = &yVal;

   //read lines in memory

   int i;

   int j = 0;
   
   struct Func *f = malloc(sizeof(struct Func));
   if(f == NULL){
       return 1;
   }

   struct Func *cursor = NULL;

    while(1){


        cursor = &f[j];

        

       i = makeFunc(x,y,fp, cursor);



       if(i == 0){
           
           
           j++;
            

            //increase space for a new func
           f = realloc(f, sizeof(struct Func)*(j+1));
           
           continue;


       }else if(i == -1){

           break;
        
       }else if(i == -2){
           
           free(cursor->oplist);
           
           f = realloc(f, sizeof(struct Func)*(j));
           
           break;
        
       }else if(i == -3){
           break;


       }else{
           break;
       }

    }


    for(int k = j - 1; k >= 0; k--){
        
        funcPrint(f[k]);
        
        free(f[k].oplist);
        
        f[k].oplist = NULL;
    }

    
    free(f);
    
    f = NULL;
    
    cursor = NULL;

   fclose(fp);
   
   return 0;
}