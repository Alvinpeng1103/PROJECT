#include "virtual_alloc.h"
#include "virtual_sbrk.h"
#include <stdio.h>
#include <inttypes.h>
#include <string.h>

#define True 1
#define False 0
#define Val 1



struct Allocator{

    uint8_t size;

    uint8_t min;

    void *blocks;

    void *data;

};

struct Block{
    uint8_t size; //total 2^size 
    
    uint8_t is_free;
    
    uint8_t tmp_free;

    uint8_t available;

    uint8_t tmp_a;

    uint8_t split;

    uint8_t tmp_split;
    
    void *address; //actual data address
    
    uint64_t buddy; //buddy index
    
};




void init_allocator(void * heapstart, uint8_t initial_size, uint8_t min_size){


    struct Allocator *header = (struct Allocator *)heapstart;

    //printf("heapstart %p\n", heapstart);
    
    uint64_t res = Val << initial_size;

    virtual_sbrk(sizeof(struct Allocator) - (virtual_sbrk(0) - heapstart));

    header->data = virtual_sbrk(sizeof(uint8_t) * res);

    //printf("data %p\n", header->data);

    header->size = initial_size;

    header->min = min_size;

    //printf("csize %d, msize %d\n", header->size, header->min);

    uint64_t nums = (Val << (initial_size - min_size + 1)) - 1;

    header->blocks = virtual_sbrk(sizeof(struct Block) * nums);

    //printf("the address is %"PRIu64"\n", nums);


    struct Block *blocks = header->blocks;

    blocks[0].address = header->data;
    blocks[0].buddy = 0;
    blocks[0].size = initial_size;
    blocks[0].split = False;
    blocks[0].tmp_split = False;
    
    blocks[0].is_free = True;
    blocks[0].tmp_free = True;
    blocks[0].available = True;
    blocks[0].tmp_a = True;

    for(uint64_t i = 1; i < nums; i++){

        blocks[i].address = NULL;
        blocks[i].buddy = 0;
        blocks[i].size = 0;
        blocks[i].split = False;
        blocks[i].tmp_split = False;
        blocks[i].is_free = True;
        blocks[i].tmp_free = True;
        blocks[i].available = False;
        blocks[i].tmp_a = False;
    }



}


uint8_t convert(uint32_t size){

    uint8_t res = 0;
    
    uint8_t num_of_one = 0;
    
    for(uint8_t i = 1; i < 32; i++){
        
        if((size & 1) == 1){
            
            res = i;
            
            num_of_one++;
        }
        size = size >> 1;
    }

    if(num_of_one == 1){
        
        res = res - 1;
    }    
    return res;
} 





uint64_t find_start(uint8_t max, uint8_t k){

    uint64_t start = 0;
    

    for(uint8_t i = max; i > k; i--){

        start = start * 2 + 1;
    }

    return start;
}

uint64_t find_end(uint64_t start, uint8_t max, uint8_t k){

    uint8_t minus = max - k;

    return start + (Val << minus) - 1;
}

void split(struct Block *blocks, uint64_t i){

    uint64_t left_child = 2 * i + 1;
    uint64_t right_child = 2 * i + 2;
    uint8_t child_size = blocks[i].size - 1;

    blocks[left_child].address = blocks[i].address;
    blocks[right_child].address = blocks[i].address + (Val << child_size);
    blocks[left_child].available = True;  
    blocks[right_child].available = True;
    blocks[left_child].tmp_a = True;  
    blocks[right_child].tmp_a = True;
    blocks[i].available = False;
    
    blocks[i].split = True;
    blocks[i].tmp_a = False;
    
    blocks[i].tmp_split = True;

    blocks[left_child].buddy = right_child;
    blocks[right_child].buddy = left_child;

    blocks[left_child].size = child_size;
    blocks[right_child].size = child_size;
}



uint64_t find_block(struct Block *blocks, uint8_t k, uint8_t max){

    uint64_t start = find_start(max, k);

    uint64_t end = find_end(start, max, k);


    //printf("The start we found is %"PRIu64"\n", start);
    //printf("The end we found is %"PRIu64"\n", end);

    for(uint64_t i = start; i <= end; i++){

        if(blocks[i].available == True){

            if(blocks[i].is_free == True){

                //printf("The index we found is %"PRIu64"\n", i);

                 return i;

            }else{

                continue;
            }
        }
    }

    return 0;

}

void* buddy_algorithm(struct Block *blocks,uint8_t k, uint8_t max){

    uint64_t loc;
    uint8_t size;

    uint8_t loop1 = 1;
    uint8_t loop2 = 1;
    
    void *res = NULL;

    while(loop1){

        size = k;
        

        loc = find_block(blocks, k, max);

        if(k == max && loc == 0){

            if(blocks[0].available == False){
                break;
            }

            blocks[0].is_free = False;
            blocks[0].tmp_free = False;
            
            res =  blocks[0].address;



            
            
            break;
        }

        else if(loc != 0){
            blocks[loc].is_free = False;
            blocks[loc].tmp_free = False;

            res =  blocks[loc].address;

            break;
        }

        else{

            while(loop2){

                

                size = size + 1;

                

                if(size == max){

                    if(blocks[0].is_free == True){

                        split(blocks, 0);

                        //go back to the first find_block

                        break;

                    }else{

                        loop1 = 0;
                        break;
                    }
                }else{
                    uint64_t parent = find_block(blocks, size, max);

                    if(parent != 0){

                        split(blocks, parent);

                        break;
                    
                    }else{

                        continue;
                    }
                }               
            }

            if(loop1 == 0){

                break;
            }

        }
        //loop1 continue

    }

    return res;

}



void * virtual_malloc(void * heapstart, uint32_t size) {
    // Your code here
    
    
    struct Allocator *cursor = (struct Allocator*)heapstart;
    
    uint8_t k = convert(size);
    
    uint8_t max = cursor->size;
    
    uint8_t min = cursor->min;

    //printf("total size is %d, now malloc size is %d\n", max, k);


    struct Block *blocks = (struct Block *)(cursor->blocks);

    if(k == 0){
        return NULL;
    }


    if(k > max){
        return NULL;
        //handle error
    }
    if(k < min){
        
        k = min;
    }



    void* res = buddy_algorithm(blocks, k, max);
    //printf("the malloc address is %p\n", res);
    return res;
        
    
}
void merge(struct Block *blocks, uint64_t i){


    uint64_t buddy_index = blocks[i].buddy;

    if(buddy_index == 0){

        return;
    }

    //printf("buddy %"PRIu64", self %"PRIu64"\n", buddy_index, i);
    //printf("self free: %d, buddy free: %d, self available %d, buddy avaialble %d\n", blocks[i].is_free, blocks[buddy_index].is_free, blocks[i].available, blocks[buddy_index].available);

    if(blocks[buddy_index].is_free == True && blocks[buddy_index].available == True && blocks[i].is_free == True && blocks[i].available == True){

        blocks[i].available = False;
        blocks[i].tmp_a = False;
        blocks[buddy_index].available = False;
        blocks[buddy_index].tmp_a = False;

        uint64_t parent;

        if(i % 2 == 0){

                parent = (i-2)/2;
            }else{
                parent = (i-1)/2;
            }



            blocks[parent].available = True;
            blocks[parent].tmp_a = True;
            blocks[parent].split = False;
            blocks[parent].tmp_split = False;

            merge(blocks, parent);
            
        }
    
}



int virtual_free(void * heapstart, void * ptr) {
    // Your code here

    //printf("free address is %p\n", ptr);

    //printf("the free address is %p\n", ptr);

    struct Allocator *heap = (struct Allocator*)heapstart;

    int k = 1;


    uint64_t total = (Val << (heap->size - heap->min + 1)) - 1;

    struct Block *blocks = heap->blocks;

    for(uint64_t i = 0; i < total; i++){

        uint8_t *block_addr = (uint8_t *)blocks[i].address;

        uint8_t *p = (uint8_t *)ptr;


        if(block_addr == p && blocks[i].available == True){
            
            k = 0;

            //printf("index is %"PRIu64"\n", i);

            blocks[i].is_free = True;
            blocks[i].tmp_free = True;

            merge(blocks, i);

        }
    }
    return k;
}



void copy_tmp(void *heapstart){

    struct Allocator *heap = (struct Allocator*)heapstart;


    uint64_t total = (Val << (heap->size - heap->min + 1)) - 1;

    struct Block *blocks = heap->blocks;

    for(uint64_t i = 0; i < total; i++){

        blocks[i].available = blocks[i].tmp_a;
        blocks[i].is_free = blocks[i].tmp_free;
        blocks[i].split = blocks[i].tmp_split;
    }


}

void fake_merge(struct Block *blocks, uint64_t i){


    uint64_t buddy_index = blocks[i].buddy;

    

    if(buddy_index == 0){

        return;
    }

    //printf("before if , buddy %"PRIu64", self %"PRIu64"\n", buddy_index, i);
    //printf("self free: %d, buddy free: %d, self available %d, buddy avaialble %d\n", blocks[i].is_free, blocks[buddy_index].is_free, blocks[i].available, blocks[buddy_index].available);

    if(blocks[buddy_index].tmp_free == True && blocks[buddy_index].tmp_a == True){

        //printf("buddy %"PRIu64", self %"PRIu64"\n", buddy_index, i);

        blocks[i].tmp_a = False;
        blocks[buddy_index].tmp_a = False;

        uint64_t parent;

        if(i % 2 == 0){

                parent = (i-2)/2;
            }else{
                parent = (i-1)/2;
            }

            blocks[parent].tmp_a = True;
            blocks[parent].tmp_split = False;

            fake_merge(blocks, parent);
            
        }
    
}

int fake_free(void *heapstart, void *ptr){
    // Your code here

    //printf("free address is %p\n", ptr);

    struct Allocator *heap = (struct Allocator*)heapstart;

    int k = 1;

    



    uint64_t total = (Val << (heap->size - heap->min + 1)) - 1;


    struct Block *blocks = heap->blocks;

    // for(uint64_t i = 0; i < total; i++){
    //     printf("the block %"PRId64" size is %d, allocated: %d, available: %d, split %d\n", i, blocks[i].size, blocks[i].is_free, blocks[i].available, blocks[i].split);
    // }

    for(uint64_t i = 0; i < total; i++){

        uint8_t *block_addr = (uint8_t *)blocks[i].address;

        uint8_t *p = (uint8_t *)ptr;


        if(block_addr == p && blocks[i].tmp_a == True){
            
            k = 0;

            blocks[i].tmp_free = True;

            fake_merge(blocks, i);
            

            

        }
    }
    return k;
}


void fake_split(struct Block *blocks, uint64_t i){

    uint64_t left_child = 2 * i + 1;
    uint64_t right_child = 2 * i + 2;
    uint8_t child_size = blocks[i].size - 1;

    blocks[left_child].address = blocks[i].address;
    blocks[right_child].address = blocks[i].address + (Val << child_size);
    blocks[left_child].tmp_a = True;  
    blocks[right_child].tmp_a = True;
    blocks[i].tmp_a = False;
    
    blocks[i].tmp_split= True;

    blocks[left_child].buddy = right_child;
    blocks[right_child].buddy = left_child;

    blocks[left_child].size = child_size;
    blocks[right_child].size = child_size;
}



uint64_t fake_find_block(struct Block *blocks, uint8_t k, uint8_t max){

    uint64_t start = find_start(max, k);

    uint64_t end = find_end(start, max, k);


    //printf("The start we found is %"PRIu64"\n", start);
    //printf("The end we found is %"PRIu64"\n", end);

    for(uint64_t i = start; i <= end; i++){

        if(blocks[i].tmp_a == True){

            if(blocks[i].tmp_free == True){

                //printf("The index we found is %"PRIu64"\n", i);

                 return i;

            }else{

                continue;
            }
        }
    }

    return 0;

}

void* fake_algorithm(struct Block *blocks,uint8_t k, uint8_t max){

    uint64_t loc;
    uint8_t size;

    uint8_t loop1 = 1;
    uint8_t loop2 = 1;
    
    void *res = NULL;

    while(loop1){

        size = k;
        

        loc = fake_find_block(blocks, k, max);

        if(k == max && loc == 0){

            blocks[0].tmp_free = False;
            
            res =  blocks[0].address;

            
            
            break;
        }

        else if(loc != 0){
            blocks[loc].tmp_free = False;

            res =  blocks[loc].address;

            break;
        }

        else{

            while(loop2){

                

                size = size + 1;

                

                if(size == max){

                    if(blocks[0].tmp_free == True){

                        fake_split(blocks, 0);

                        //go back to the first find_block

                        break;

                    }else{

                        loop1 = 0;
                        break;
                    }
                }else{
                    uint64_t parent = fake_find_block(blocks, size, max);

                    if(parent != 0){

                        fake_split(blocks, parent);

                        break;
                    
                    }else{

                        continue;
                    }
                }               
            }

            if(loop1 == 0){

                break;
            }

        }
        //loop1 continue

    }

    return res;

}

uint8_t find_original_size(void * heapstart, void * ptr){

    struct Allocator *heap = (struct Allocator*)heapstart;


    uint64_t total = (Val << (heap->size - heap->min + 1)) - 1;

    struct Block *blocks = heap->blocks;

    for(uint64_t i = 0; i < total; i++){

        uint8_t *block_addr = (uint8_t *)blocks[i].address;

        uint8_t *p = (uint8_t *)ptr;


        if(block_addr == p && blocks[i].available == True){
            
            return blocks[i].size;

        }
    }
    return 0;
}

void copy_origin(void *heapstart){

    struct Allocator *heap = (struct Allocator*)heapstart;


    uint64_t total = (Val << (heap->size - heap->min + 1)) - 1;

    struct Block *blocks = heap->blocks;

    for(uint64_t i = 0; i < total; i++){

        blocks[i].tmp_a = blocks[i].available;
        blocks[i].tmp_free = blocks[i].is_free;
        blocks[i].tmp_split = blocks[i].split;
    }


}


void * fake_malloc(void * heapstart, uint32_t size) {

    //printf("now realloc size is %"PRId32"\n", size);
    // Your code here
    
    struct Allocator *cursor = (struct Allocator*)heapstart;
    uint8_t k = convert(size);
    
    uint8_t max = cursor->size;
    
    uint8_t min = cursor->min;


    struct Block *blocks = (struct Block *)(cursor->blocks);

    if(k == 0){
        return NULL;
    }


    if(k > max){
        return NULL;
        //handle error
    }
    if(k < min){
        
        k = min;
    }



    return fake_algorithm(blocks, k, max);
        
    
}



void * virtual_realloc(void * heapstart, void * ptr, uint32_t size) {

    // Your code here
    if(size == 0){
        return NULL;
    }
    

    if(fake_free(heapstart, ptr) != 0){
        return NULL;
    }

    // struct Allocator *tmp = (struct Allocator*)heapstart;

    // struct Block *blocks = tmp->blocks;

    // uint64_t total = (Val << (tmp->size - tmp->min + 1)) - 1;

    // for(uint64_t i = 0; i < total; i++){
    //     printf("the block %"PRId64" size is %d, allocated: %d, available: %d, split %d\n", i, blocks[i].size, blocks[i].tmp_free, blocks[i].tmp_a, blocks[i].tmp_split);
    // }



    void *res = fake_malloc(heapstart, size);

    if(res == NULL){
        return NULL;
    }

    uint8_t t = find_original_size(heapstart, ptr);

    uint64_t x = Val << t;

    void *value = memcpy(res, ptr, x);

    copy_tmp(heapstart);

    
    return value;
}



void PRINT(struct Block *blocks, uint64_t i){
    if(blocks[i].split == False){


        if(blocks[i].is_free == True){

                uint64_t size = (Val << blocks[i].size);

                //printf("the address is %p\n", blocks[i].address);

                printf("free %"PRIu64"\n", size);
                return;

            }else{
                uint64_t size = (Val << blocks[i].size);
                //printf("the address is %p\n", blocks[i].address);
                printf("allocated %"PRIu64"\n", size);
                return;
            }

    }
    PRINT(blocks, (2*i + 1));
    PRINT(blocks, (2*i + 2));

}



void virtual_info(void * heapstart) {
    // Your code here

    struct Allocator* heap = (struct Allocator*)heapstart;

    struct Block * blocks = (struct Block*)heap->blocks;


    PRINT(blocks, 0);


}