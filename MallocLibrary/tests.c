#include "virtual_alloc.h"
#include "virtual_sbrk.h"
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>




void * virtual_heap = NULL;
void * ptr = NULL;

void * virtual_sbrk(int32_t increment) {
    // Your implementation here (for your testing only
    brk(ptr + increment);

    ptr = sbrk(0);

   

    return ptr; 
}

void test1(){
    

    

    virtual_heap = sbrk(0);
    
    ptr = virtual_heap;

    init_allocator(virtual_heap, 12, 8);

    virtual_malloc(virtual_heap, 4095);

    FILE *fp;

    fp = freopen("testcases/test1.out", "w+", stdout);

    virtual_info(virtual_heap);

    fclose(fp);

}

/*malloc the size which is bigger than maximum size*/
void test2(){

    virtual_heap = sbrk(0);
    
    ptr = virtual_heap;

    init_allocator(virtual_heap, 12, 8);

    virtual_malloc(virtual_heap, 6000);

    FILE *fp;

    fp = freopen("testcases/test2.out", "w+", stdout);

    virtual_info(virtual_heap);

    fclose(fp);


}

void test3(){

    virtual_heap = sbrk(0);
    
    ptr = virtual_heap;

    init_allocator(virtual_heap, 12, 8);

    
    FILE *fp;

    fp = freopen("testcases/test3.out", "w+", stdout);
    void *p1 = virtual_malloc(virtual_heap, 256);
    void *p2 = virtual_malloc(virtual_heap, 256);
    void *p3 = virtual_malloc(virtual_heap, 256);
    virtual_info(virtual_heap);
    virtual_free(virtual_heap, p1);
    virtual_info(virtual_heap);
    virtual_free(virtual_heap, p2);
    virtual_info(virtual_heap);
    virtual_free(virtual_heap, p3);
    virtual_info(virtual_heap);

    fclose(fp);

}

void test4(){
    virtual_heap = sbrk(0);
    
    ptr = virtual_heap;

    init_allocator(virtual_heap, 12, 11);

    
    FILE *fp;

    fp = freopen("testcases/test4.out", "w+", stdout);
    void *p1 = virtual_malloc(virtual_heap, 4096);
    virtual_info(virtual_heap);
    virtual_malloc(virtual_heap, 2048);
    virtual_info(virtual_heap);
    virtual_free(virtual_heap, p1);
    virtual_info(virtual_heap);

    fclose(fp);
    
}

void test5(){

    virtual_heap = sbrk(0);
    
    ptr = virtual_heap;

    init_allocator(virtual_heap, 12, 1);

    
    FILE *fp;

    fp = freopen("testcases/test5.out", "w+", stdout);
    void *p1 = virtual_malloc(virtual_heap, 2);
    virtual_info(virtual_heap);
    virtual_free(virtual_heap, p1);
    virtual_info(virtual_heap);

    fclose(fp);

    



}

void test6(){

    virtual_heap = sbrk(0);
    
    ptr = virtual_heap;

    init_allocator(virtual_heap, 12, 8);

    
    FILE *fp;

    fp = freopen("testcases/test6.out", "w+", stdout);
    void *p1 = virtual_malloc(virtual_heap, 2048);
    virtual_info(virtual_heap);
    virtual_realloc(virtual_heap, p1, 2000);
    virtual_info(virtual_heap);
    virtual_free(virtual_heap, p1);
    virtual_info(virtual_heap);

    fclose(fp);



}

void test7(){

    virtual_heap = sbrk(0);
    
    ptr = virtual_heap;

    init_allocator(virtual_heap, 12, 8);

    
    FILE *fp;

    fp = freopen("testcases/test7.out", "w+", stdout);
    void *p1 = virtual_malloc(virtual_heap, 256);
    virtual_info(virtual_heap);
    void *p2 = virtual_malloc(virtual_heap, 256);
    virtual_info(virtual_heap);
    virtual_free(virtual_heap, p1);
    virtual_info(virtual_heap);
    void *p3 = virtual_malloc(virtual_heap, 256);
    virtual_info(virtual_heap);
    virtual_free(virtual_heap, p2);
    virtual_free(virtual_heap, p3);
    virtual_info(virtual_heap);

    fclose(fp);


}

void test8(){

    virtual_heap = sbrk(0);
    
    ptr = virtual_heap;

    init_allocator(virtual_heap, 12, 8);

    
    FILE *fp;

    fp = freopen("testcases/test8.out", "w+", stdout);
    void *p1 = virtual_malloc(virtual_heap, 2048);
    virtual_malloc(virtual_heap, 1024);
    virtual_info(virtual_heap);
    virtual_free(virtual_heap, p1);
    virtual_info(virtual_heap);

    fclose(fp);


}

void test9(){

    virtual_heap = sbrk(0);
    
    ptr = virtual_heap;

    init_allocator(virtual_heap, 12, 11);

    
    FILE *fp;

    fp = freopen("testcases/test9.out", "w+", stdout);
    void *p1 = virtual_malloc(virtual_heap, 4096);
    virtual_info(virtual_heap);
    virtual_malloc(virtual_heap, 2048);
    virtual_info(virtual_heap);
    virtual_free(virtual_heap, p1);
    virtual_info(virtual_heap);

    fclose(fp);

}


// void test10(){
//     virtual_heap = sbrk(0);
    
//     ptr = virtual_heap;

//     init_allocator(virtual_heap, 12, 8);

//     FILE *fp;

//     fp = freopen("testcases/test3.expected", "w+", stdout);

//     void *p1 = virtual_malloc(virtual_heap, 4096);

//     virtual_info(virtual_heap);

//     virtual_realloc(virtual_heap, p1, 2048);

//     virtual_info(virtual_heap);

//     void *p2 = virtual_malloc(virtual_heap, 256);

//     virtual_info(virtual_heap);

//     virtual_free(virtual_heap, p1);

//     virtual_info(virtual_heap);


//     virtual_realloc(virtual_heap, p2, 1024);

//     virtual_info(virtual_heap);

//     virtual_free(virtual_heap, p2);

//     virtual_info(virtual_heap);

//     fclose(fp);
// }




int main() {
    //Your own testing code here

    test1();
    test2();
    test3();
    test4();
    test5();
    test6();
    test7();
    test8();
    test9();



    return 0;
}
