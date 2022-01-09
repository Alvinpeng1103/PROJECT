#include "btreestore.h"
#include <stdlib.h>

int main() {
    // Your own testing code here

    //I cannot tr
    void * helper = init_store(4, 4);

    uint64_t* data = malloc(sizeof(uint64_t) * 2);

    data[0] = 1;
    data[1] = 2;

    uint32_t key = 9;

    uint32_t *encryption_key = malloc(sizeof(uint32_t) * 4);

    struct node **list = malloc(sizeof(struct node *));



    btree_insert(key, (void*)data, sizeof(uint64_t) * 2, encryption_key, 1, helper);

    btree_export(helper, list);

    close_store(helper);

    return 0;
}
