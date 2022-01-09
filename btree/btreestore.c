#include "btreestore.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#include <pthread.h>


void *init_store(uint16_t branching, uint8_t n_processors)
{
    
    //allocate space for tree 
    struct Tree *b_tree = malloc(sizeof(struct Tree));
    //branching
    b_tree->branching = branching;
    //threads
    b_tree->n_processors = n_processors;
    //root node
    b_tree->root = NULL;
    
    //b_tree->threads = malloc(sizeof(pthread_t) * n_processors);

    //create thread


    return (void *)b_tree;
}
void free_node(struct TreeNode **target)
{
    //free the "keys" pointer
    free((*target)->key_info.keys);

    for (uint16_t i = 0; i < (*target)->info_nums; i++)
    {   

        //free each info's data pointer and its pointer
        free((*target)->info_list[i]->data);
        (*target)->info_list[i]->data = NULL;
        free((*target)->info_list[i]);
        (*target)->info_list[i] = NULL;
    }
    //free the info list pointer
    free((*target)->info_list);

    (*target)->info_list = NULL;

    (*target)->parent = NULL;

    //free the node itself
    free(*target);

    *target = NULL;
}
void free_recursion(struct TreeNode **node)
{
    //if the node is leaf node, then we can free it
    if ((*node)->children == NULL)
    {   
        //free the leaf node itself
        free_node(node);

        return;
    }

    for (uint16_t i = 0; i < (*node)->child_nums; i++)
    {
        
        free_recursion(&(*node)->children[i]);
        
    }
    //after free all the child node, we free the pointer of children list
    free((*node)->children);
    (*node)->children = NULL;

    //Then we free the internal node itself
    free_node(node);

    //return to the parent of internal node
    return;
}

void close_store(void *helper)
{
    // Your code here
    struct Tree *b_tree = (struct Tree *)helper;

    b_tree->branching = 0;
    b_tree->n_processors = 0;
    
    //free all the node
    free_recursion(&b_tree->root);
    
    //free tree
    free(b_tree);
    return;
}

int find_key(struct TreeNode *root, uint32_t key, struct TreeNode **target_node, uint16_t *target_index)
{

    uint16_t index; //it is used to keep the index of current node
    int found; //it indicates that whether the key is in the rightmost child node or not
    struct TreeNode *cursor = root;

    while (cursor->children != NULL)
    {

        index = 0;
        found = 0;

        for (uint16_t i = 0; i < cursor->key_info.num_keys; i++)
        {
            //if key == the ith key in the cursor's key list
            //the key is in the internal node
            if (key == cursor->key_info.keys[i])
            {   
                //get the result
                *target_node = cursor;
                *(target_index) = i;
                return 1;
            }
            //if the key is less than the ith key in the cursor's
            if (key < cursor->key_info.keys[i])
            {
                //key is in de child node
                index = i;
                found = 1;
                break;
            }
        }
        if (found == 1)
        {   //key is in one child node except for the rightmost 
            cursor = cursor->children[index];
        }
        else
        {   //key is in the rightmost of child nodes
            cursor = cursor->children[cursor->key_info.num_keys];
        }
    }
    //the key is in the leaf node
    for (uint16_t i = 0; i < cursor->key_info.num_keys; i++)
    {

        if (key == cursor->key_info.keys[i])
        {

            *target_node = cursor;
            *(target_index) = i;
            return 1;
        }
    }
    return 0;
}

int check_exist(struct TreeNode *cursor, uint32_t key, struct TreeNode **result, uint16_t *pos)
{
    //it is similar to the "find_key", but if we find the key exists, we return -1
    uint16_t index;
    int found;

    if (cursor->children == NULL)
    {

        *result = cursor;
        index = 0;
        found = 0;

        for (uint16_t i = 0; i < cursor->key_info.num_keys; i++)
        {

            if (key == cursor->key_info.keys[i])
            {
                return -1;
            }

            if (key < cursor->key_info.keys[i])
            {
                index = i;
                found = 1;
                break;
            }
        }
        //we found the place for new key
        if (found == 1)
        {
            *pos = index;

            return 0;
        }
        else
        {
            *pos = cursor->key_info.num_keys;
            return 0;
        }
    }
    else
    {

        index = 0;
        found = 0;

        for (uint16_t i = 0; i < cursor->key_info.num_keys; i++)
        {

            if (key == cursor->key_info.keys[i])
            {
                return -1;
            }

            if (key < cursor->key_info.keys[i])
            {

                index = i;
                found = 1;
                break;
            }
        }
        if (found == 1)
        {
            if (check_exist(cursor->children[index], key, result, pos) == -1)
            {
                return -1;
            }
        }
        else
        {
            if (check_exist(cursor->children[cursor->key_info.num_keys], key, result, pos) == -1)
            {
                return -1;
            }
        }
    }
    return 0;
}

void search_place(uint32_t key, uint16_t *pos, struct TreeNode *parent)
{   
    //it is used for searching the position(index) of node in its parent's children list
    for (uint16_t i = 0; i < parent->key_info.num_keys; i++)
    {
        
        if (key < parent->key_info.keys[i])
        {

            *pos = i;
            return;
        }
    }
    *pos = parent->key_info.num_keys;
}

int insert_key(uint32_t key, uint16_t pos, struct TreeNode **current)
{

    //insert one key  and sort them in increasing order

    if ((*current)->key_info.keys == NULL)
    {
        return -1;
    }

    int j = (*current)->key_info.num_keys;

    while (j > pos)
    {
        (*current)->key_info.keys[j] = (*current)->key_info.keys[j - 1];
        j--;
    }

    (*current)->key_info.keys[j] = key;

    (*current)->key_info.num_keys = (*current)->key_info.num_keys + 1;

    return 0;
}

int insert_info(struct info *p_info, uint16_t pos, struct TreeNode **current)
{
    //insert one info and  sort them in increasing order
    if ((*current)->info_list == NULL)
    {
        return -1;
    }

    int j = (*current)->info_nums;

    while (j > pos)
    {
        (*current)->info_list[j] = (*current)->info_list[j - 1];
        j--;
    }

    (*current)->info_list[j] = p_info;

    (*current)->info_nums = (*current)->info_nums + 1;

    return 0;
}


//we made two new node, copy data from the old node to them, add the median key and info to its parent, then delete old node
void split(struct TreeNode **current_node, uint16_t *median, uint32_t *median_key, uint16_t branching, struct TreeNode **root)
{

    //find the median index, pass it to the argument
    *median = ((*current_node)->key_info.num_keys - 1) / 2;

    //find the median key value, pass it to the argument
    *median_key = (*current_node)->key_info.keys[*median];

    //the median key - info
    struct info *median_info = (*current_node)->info_list[*median];

    //parent node
    struct TreeNode *parent = (*current_node)->parent;


    //create a new node for left side
    struct TreeNode *leftnode = malloc(sizeof(struct TreeNode));

    //create a new node for right side
    struct TreeNode *rightnode = malloc(sizeof(struct TreeNode));


    //first we need to copy data from the old node to new left node and right node

    //copy right key value
    uint32_t *right_pointer = (*current_node)->key_info.keys + (*median) + 1;
    //right key's num
    uint16_t right_nums = (*current_node)->key_info.num_keys - (*median + 1);
    //allocate sufficient key space
    rightnode->key_info.keys = malloc(sizeof(uint32_t) * branching);
    //copy key's data
    memcpy(rightnode->key_info.keys, right_pointer, sizeof(uint32_t) * right_nums);

    rightnode->key_info.num_keys = right_nums;

    //copy right info
    struct info **right_info_pointer = (*current_node)->info_list + (*median) + 1;

    uint16_t right_info_nums = (*current_node)->info_nums - (*median + 1);

    rightnode->info_list = malloc(sizeof(struct info *) * branching);

    memcpy(rightnode->info_list, right_info_pointer, sizeof(struct info *) * right_info_nums);

    rightnode->info_nums = right_info_nums;


    
    if((*current_node)->children != NULL){

        //copy right children
        uint16_t right_child_nums = (*current_node)->child_nums - (*median + 1);

        struct TreeNode **right_child_pointer = (*current_node)->children + (*median + 1);

        rightnode->children = malloc(sizeof(struct TreeNode *) * branching);

        

        memcpy(rightnode->children, right_child_pointer, sizeof(struct TreeNode *) * right_child_nums);

        rightnode->child_nums = right_child_nums;


        
    }else{
        //leaf node
        rightnode->children = NULL;
        rightnode->child_nums = 0;
    }

        

    //set parent
    rightnode->parent = parent;

    //copy left key value
    uint32_t *left_pointer = (*current_node)->key_info.keys;

    uint16_t left_nums = *median;

    leftnode->key_info.keys = malloc(sizeof(uint32_t) * branching);

    memcpy(leftnode->key_info.keys, left_pointer, sizeof(uint32_t) * left_nums);

    leftnode->key_info.num_keys = left_nums;

    //copy left info
    struct info **left_info_pointer = (*current_node)->info_list;

    uint16_t left_info_nums = *median;

    leftnode->info_list = malloc(sizeof(struct info *) * branching);

    memcpy(leftnode->info_list, left_info_pointer, sizeof(struct info *) * left_info_nums);

    leftnode->info_nums = left_info_nums;


    if((*current_node)->children != NULL){

        //copy left children
        uint32_t left_child_nums = *median + 1;

        struct TreeNode **left_child_pointer = (*current_node)->children;

        leftnode->children = malloc(sizeof(struct TreeNode *) * branching);

        memcpy(leftnode->children, left_child_pointer, sizeof(struct TreeNode *) * left_child_nums);

        leftnode->child_nums = left_child_nums;

       

        

    }else{
        //left node is leaf node
        leftnode->children = NULL;
        leftnode->child_nums = 0;
    }

    leftnode->parent = parent;

    

    //This current node is old root, so we need to create new root node
    if (parent == NULL)
    {

        //allocate newspce for the new root
        struct TreeNode *newroot = malloc(sizeof(struct TreeNode));

        //add median key
        newroot->key_info.keys = malloc(sizeof(uint32_t) * branching);
    
        newroot->key_info.keys[0] = *median_key;

        newroot->key_info.num_keys = 1;
        
        
        //add info
        newroot->info_list = malloc(sizeof(struct info *) * branching);

        newroot->info_list[0] = median_info;

        newroot->info_nums = 1;

        //set parent
        newroot->parent = NULL;

        //add children
        newroot->children = malloc(sizeof(struct TreeNode *) * 2);

        newroot->children[0] = leftnode;

        newroot->children[1] = rightnode;

        newroot->child_nums = 2;

        newroot->children[0]->parent = newroot;
        newroot->children[1]->parent = newroot;

        //set root to new root
        *root = newroot;


    }
    else
    {
        //we need to insert median key to parent node
        uint16_t insert_index;

        
        search_place(*median_key, &insert_index, parent);

        insert_key(*median_key, insert_index, &parent);


        insert_info(median_info, insert_index, &parent);

       


        //insert left child and right child to parent
        parent->children = realloc(parent->children, sizeof(struct TreeNode *) * (parent->child_nums + 1));

        uint16_t j = parent->child_nums;

    
        //sort the child
        while (j > insert_index + 1)
        {
            parent->children[j] = parent->children[j - 1];
            j--;
        }

        parent->children[j] = rightnode;

        

        parent->children[j - 1] = leftnode;

        parent->child_nums = parent->child_nums + 1;

        

    }

    //free the old node
    struct TreeNode *tmp = *current_node;
    *current_node = parent;

    free(tmp->key_info.keys);
    free(tmp->children);
    free(tmp->info_list);
    free(tmp);
    tmp = NULL;
}

int btree_insert(uint32_t key, void *plaintext, size_t count, uint32_t encryption_key[4], uint64_t nonce, void *helper)
{
    /*---------------------OK-------------------------*/

   
    //convert helper to tree pointer
    struct Tree *btree = (struct Tree *)helper;

    struct TreeNode *root = btree->root;

    uint16_t branching = btree->branching;

    //it stores the node that key can be stored in
    struct TreeNode *result = NULL;

    //it stores the index(position) of the new key in key array
    uint16_t pos = 0;

    //the nums of block
    uint32_t nums_block;

    if (count != 0)
    {
        nums_block = (count / sizeof(uint64_t)) + 1;
    }
    else
    {
        nums_block = 0;
    }

    /*--------------------OK-----------------------*/

    //make new info
    struct info *p_info = malloc(sizeof(struct info));

    p_info->nonce = nonce;

    p_info->size = count;

    memcpy(p_info->key, encryption_key, sizeof(uint32_t) * 4);

    uint64_t *cipher_text = malloc(sizeof(uint64_t) * nums_block);

    uint64_t *plain_text = malloc(sizeof(uint64_t) * nums_block);

    memcpy((void *)plain_text, plaintext, count);

    encrypt_tea_ctr(plain_text, encryption_key, nonce, cipher_text, nums_block);

    p_info->data = (void *)cipher_text;

    free(plain_text);

    /*insert the first node in the tree*/

    if (btree->root == NULL)
    {

        btree->root = malloc(sizeof(struct TreeNode));

        btree->root->parent = NULL;

        btree->root->key_info.keys = malloc(sizeof(uint32_t) * (branching));

        btree->root->key_info.keys[0] = key;

        btree->root->key_info.num_keys = 1;

        btree->root->child_nums = 0;

        btree->root->children = NULL;

        btree->root->info_list = malloc(sizeof(struct info *) * (branching));

        btree->root->info_list[0] = p_info;

        btree->root->info_nums = 1;


        return 0;
    }

    /*--------------------OK-----------------------*/

    //check if there is place for insertion
    int i = check_exist(root, key, &result, &pos);

    //if the key exists, return -1
    if (i == -1)
    {

        return -1;
    }

    //we can make key insertion on the result(node)
    if (result != NULL)
    {

        //median index in the current node
        uint16_t median;

        //median key value in the current node
        uint32_t median_key;

        //insert key in the current node
        insert_key(key, pos, &result);

        //fprintf(stderr, "591 result key number %d, first key is %d\n", result->key_info.num_keys, result->key_info.keys[0]);

        insert_info(p_info, pos, &result);

        
        //continue to split 
        while (result != NULL && result->key_info.num_keys == branching)
        {   
            
            split(&result, &median, &median_key, branching, &(btree->root));
        }

        return 0;
    }

    return -1;
}

int btree_retrieve(uint32_t key, struct info *found, void *helper)
{
    // Your code here
    //convert helper to tree pointer
    struct Tree *btree = (struct Tree *)helper;

    //get the root
    struct TreeNode *root = btree->root;

    //get the branching
    uint16_t branching = btree->branching;

    struct TreeNode *result = NULL;

    uint16_t key_index = 0;

    //we can find key
    if (find_key(root, key, &result, &key_index) == 0)
    {   
        
        return 1;
    }

    if (result != NULL)
    {

        struct info *i = result->info_list[key_index];

        //copy data from info to "found"
        memcpy(found, i, sizeof(struct info));



        return 0;
    }

    return 1;
}

int btree_decrypt(uint32_t key, void *output, void *helper)
{

    
    //convert helper to tree pointer
    struct Tree *btree = (struct Tree *)helper;

    //get the root
    struct TreeNode *root = btree->root;

    //get the branching
    uint16_t branching = btree->branching;

    struct TreeNode *result = NULL;

    uint16_t key_index = 0;

    //check if we can find the key
    if (find_key(root, key, &result, &key_index) == 0)
    {   
        
        return 1;
    }

    if (result != NULL)
    {   
        
        uint32_t nums_block;
        
        struct info *i = result->info_list[key_index];

        
        if (i->size != 0)
        {
            nums_block = (i->size / sizeof(uint64_t)) + 1;
        }
        else
        {
            nums_block = 0;
        }

        uint64_t *data = (uint64_t *)(i->data);
        
        //we need to make padding for plain text
        uint64_t *plain_text = malloc(sizeof(uint64_t) * nums_block);

        decrypt_tea_ctr(data, i->key, i->nonce, plain_text, nums_block);

        //copy plain text to output
        memcpy(output, (void *)plain_text, i->size);


        //free the pointer of plain text
        free(plain_text);

        plain_text = NULL;

        return 0;
    }

    return 1;
}

/**************

Delete Part


****************/

// void find_largest_key(struct TreeNode *node, struct TreeNode **target, uint16_t *index){

//     struct TreeNode *child;
//     uint16_t pos;

//     while(node->children != NULL){
//         pos = node->child_nums - 1;
        
//         child = node->children[pos];

//     }
//     //when the node is leaf node
//     *target = node;
//     *index = node->key_info.keys[node->key_info.num_keys - 1];
//     return;
        
// }

// void get_pos(struct TreeNode *node, uint16_t *pos){

//     struct TreeNode *parent = node->parent;

//     for(uint16_t i = 0; i < parent->child_nums; i++){

//         if(node == parent->children[i]){

//             *pos = i;

//         }
        
//     }
// }

// void swap_key(struct TreeNode *node1, struct TreeNode *node2, uint16_t index1, uint16_t index2){
//     //swap the info and key between two nodes
//         uint16_t tmp_key = node1->key_info.keys[index1];
//         struct info* tmp_info = node2->info_list[index1];
        
//         node1->key_info.keys[index1] = T->key_info.keys[index2];
//         node1->info_list[index1] = T->info_list[index2];

//         node2->key_info.keys[index2] = tmp_key;
//         node2->info_list[index2] = tmp_info;
// }

// void move_key(struct TreeNode *node1, struct TreeNode *node2, uint16_t index1, uint16_t index2){
        
//         node1->key_info.keys[index1] = node2->key_info.keys[index2];
//         node1->info_list[index1] = node2->info_list[index2];

//         for(uint16_t i = index2; i < node2->key_info.num_keys - 1; i--){

//             node2->key_info.keys[i] = node2->key_info.keys[i+1];
//             node2->info_list[i] = node2->info_list[i+1];
//         }
        
//         node2->info_nums = node2->info_nums - 1;
//         node2->key_info.num_keys = node2->key_info.num_keys - 1;   
    
// }

// void delete_empty(uint16_t index, struct TreeNode* node){
//      //delete complete
//         uint16_t i;

//         for(i = index; i < node->key_info.num_keys - 1; i++){

//             node->key_info.keys[i] = node->key_info.keys[i+1];
//             node->info_list[i] = node->info_list[i+1];

//         }

//         node->info_list[i] = NULL;
//         node->key_info.keys[i] = 0;

//         (node->key_info.num_keys)--;
//         (node->info_nums)--;

// }

int btree_delete(uint32_t key, void *helper)
{
    // // Set up root and branching
    // struct TreeNode *root;
    // uint16_t branching;
    // root = (((struct Tree *)helper)->root);
    // branching = (((struct Tree *)helper)->branching);
    
    // //Target node (current node for operations)
    // struct TreeNode *target = NULL;
    
    // //deleted key's index
    // uint16_t index;

    // //target node 's position in parent.children
    // uint16_t pos;

    // //if we cannot find the key, we return -1
    // if(find_key(root, key, &target, &index) == 0){
    //     return -1;
    // }

    // //when the key is in an internal node
    // if(target->children != NULL){

    //     //get the node C
    //     struct TreeNode *C = target->children[index];

        
    //     //find the larget key rooted in subtree of c, the key must be in the leaf node T
    //     struct TreeNode *T;
    //     uint16_t larget_key_index;

    //     find_largest_key(C, &T, &larget_key_index);

    //     //swap the info and key between K and T
    //     uint16_t tmp_key = target->key_info.keys[index];
    //     struct info* tmp_info = target->info_list[index];
        
    //     target->key_info.keys[index] = T->key_info.keys[larget_key_index];
    //     target->info_list[index] = T->info_list[larget_key_index];

    //     T->key_info.keys[larget_key_index] = tmp_key;
    //     T->info_list[larget_key_index] = tmp_info;

    //     //Change the target K's node to T
    //     target = T;

    //     //change target K's key index
    //     index = larget_key_index; 

    // }

    // //delete K's key and index
    // target->key_info.keys[index] = 0;

    // //delete pointer to data
    // free(target->info_list[index]->data);

    // //delete pointer to info
    // free(target->info_list[index]);
    // target->info_list[index] = NULL;



    // if(target->key_info.num_keys - 1 != 0){

    //     delete_empty(index, target);

       
    //     return 0;
    // }

    // //leaf node has no key

    // while(target != root){

    //     struct TreeNode* parent;
    //     struct TreeNode* left_sibling = NULL;
    //     struct TreeNode* right_sibling = NULL;

    //     if(target->children == NULL){
    //         //now target node is leaf node

    //         //get target node's pos
    //         get_pos(target, &pos);

    //         //if the node is leftmost
    //         if(pos == 0){
    //             //check right sibling

    //             right_sibling = target->parent->children[1];

    //             //if we can take one key from the right sibling
    //             if(right_sibling->key_info.num_keys - 1 > 0){

    //                 //get the smallest key in the right sibling, and exchange with the K_right

    //                 swap_key(right_sibling, target->parent, 0, 0);

    //                 //move k_right to the target node

    //                 swap_key(target, right_sibling, 0, 0);

    //                 //delete empty in right sibling
    //                 delete_empty(0, right_sibling);

    //                 //finish

    //                 return 0;

                
    //             }
                    
    //         }

    //         //if the node is rightmost
    //         else if(pos == target->parent->child_nums - 1){

    //             //check left sibling

    //             left_sibling = target->parent->children[pos-1];

    //             //if we can take one key from the left sibling
    //             if(left_sibling->key_info.num_keys - 1 > 0){

    //                 //get the biggest key in the left sibling, and exchange with the K_right

    //                 swap_key(left_sibling, parent, left_sibling->key_info.num_keys - 1, parent->key_info.keys - 1);

    //                 //move k_right to the target node

    //                 swap_key(target, left_sibling, 0, left_sibling->key_info.num_keys - 1);

    //                 //finish
    //                 delete_empty(left_sibling, left_sibling->key_info.num_keys - 1);

    //                 return 0;

                
    //             }

    //         }

    //         else{

    //             //check left sibling

    //             left_sibling = target->parent->children[pos-1];

    //             //if we can take one key from the left sibling
    //             if(left_sibling->key_info.num_keys - 1 > 0){

    //                 //get the biggest key in the left sibling, and exchange with the K_right

    //                 swap_key(left_sibling, parent, left_sibling->key_info.num_keys - 1, parent->key_info.keys - 1);

    //                 //move k_right to the target node

    //                 swap_key(target, left_sibling, 0, left_sibling->key_info.num_keys - 1);

    //                 //finish
    //                 delete_empty(left_sibling, left_sibling->key_info.num_keys - 1);

    //                 return 0;

                
    //             }
                    
                

    //             //check right sibling

    //             right_sibling = target->parent->children[pos+1];

    //             //if we can take one key from the right sibling
    //             if(right_sibling->key_info.num_keys - 1 > 0){

    //                 //get the smallest key in the right sibling, and exchange with the K_right

    //                 swap_key(right_sibling, target->parent, 0, 0);

    //                 //move k_right to the target node

    //                 swap_key(target, right_sibling, 0, 0);

    //                 //delete empty in right sibling
    //                 delete_empty(0, right_sibling);

    //                 //finish

    //                 return 0;

                
    //             }


    //         }


    //     }else{

    //         //this is for internal node
    //         parent = target->parent;
    //         left_sibling = parent->children[pos];
    //         right_sibling = parent->children[pos+1];

    //         if(left_sibling->key_info.num_keys >  (branching / 2) - 1){

    //             //we can move one key from the left sibling

    //             //find largest child
    //             struct TreeNode *left_child = left_sibling->children[left_sibling->child_nums - 1];

    //             uint16_t key_left_child = left_sibling->key_info.num_keys - 1;

    //             //move pos(K_left) to the target

    //             target->key_info.keys[index] = parent->key_info.keys[pos];

    //             //move  key_left_child to parent

    //             parent->key_info.keys[pos] = left_sibling->key_info.keys[key_left_child];


    //             //move left child to target 
    //             target->children[0] = left_child;

    //             return 0;


    //         }

    //         if(right_sibling->key_info.num_keys > (branching / 2) - 1){

    //             //we can move one key from the right sibling

    //             //we can move one key from the left sibling

    //             //find largest child
    //             struct TreeNode *left_child = left_sibling->children[left_sibling->child_nums - 1];

    //             uint16_t key_left_child = left_sibling->key_info.num_keys - 1;

    //             //move pos(K_left) to the target

    //             target->key_info.keys[index] = parent->key_info.keys[pos];

    //             //move  key_left_child to parent

    //             parent->key_info.keys[pos] = left_sibling->key_info.keys[key_left_child];


    //             //move left child to target 
    //             target->children[0] = left_child;

    //             return 0;
    //         }

    //     }


    //     //if there is no sibling node

    //     if(pos == 0){

    //         right_sibling = target->parent->children[1];

    //         //move all keys and children from right sibling to target node
    //         target->key_info.keys[index] = parent->key_info.keys[pos];

    //         //memcpy
    //         memcpy(target->key_info.keys + index + 1, right_sibling->key_info.keys, right_sibling->key_info.num_keys);

    //         //copy the child 

            

            


    //     }else{

    //         left_sibling = target->parent->children[pos-1];
    //     }

    // }

    // //if the current is root

    
    




    return -1;
}

void recursion(struct TreeNode *treenode, struct node **list, uint64_t *size)
{   

    //use pre-order method 
    
    //increase size
    *size = *size + 1;


    //resize list for a new key_node
    *list = realloc(*list, sizeof(struct node) * (*size));

    (*list)[*size - 1].num_keys = treenode->key_info.num_keys;

    (*list)[*size - 1].keys = malloc(sizeof(uint32_t) * (treenode->key_info.num_keys));

    

    memcpy((*list)[*size - 1].keys, treenode->key_info.keys, sizeof(uint32_t) * (treenode->key_info.num_keys));

    
    if(treenode->children != NULL){
        for (uint16_t i = 0; i < treenode->child_nums; i++)
    {   

        recursion(treenode->children[i], list, size);
    }

    }
    
    
    
}

uint64_t btree_export(void *helper, struct node **list)
{
    // Your code here
    struct Tree *tree = (struct Tree *)helper;

    if (tree->root == NULL)
    {
        return 0;
    }

    struct TreeNode *root = tree->root;

    uint64_t size = 0;

    recursion(root, list, &size);


    return size;
}

void encrypt_tea(uint32_t plain[2], uint32_t cipher[2], uint32_t key[4])
{
    // Your code here
    uint32_t sum = 0;
    uint32_t tmp1;
    uint32_t tmp2;
    uint32_t tmp3;
    uint32_t tmp4;
    uint32_t tmp5;
    uint32_t tmp6;

    uint32_t delta = 0x9E3779B9;

    cipher[0] = plain[0];
    cipher[1] = plain[1];

    int i = 0;
    while (i < 1024)
    {

        sum = (sum + delta) % (uint32_t)pow(2, 32);
        tmp1 = ((cipher[1] << 4) + key[0]) % (uint32_t)pow(2, 32);
        tmp2 = (cipher[1] + sum) % (uint32_t)pow(2, 32);
        tmp3 = ((cipher[1] >> 5) + key[1]) % (uint32_t)pow(2, 32);
        cipher[0] = (cipher[0] + (tmp1 ^ tmp2 ^ tmp3)) % (uint32_t)pow(2, 32);
        tmp4 = ((cipher[0] << 4) + key[2]) % (uint32_t)pow(2, 32);
        tmp5 = (cipher[0] + sum) % (uint32_t)pow(2, 32);
        tmp6 = ((cipher[0] >> 5) + key[3]) % (uint32_t)pow(2, 32);
        cipher[1] = (cipher[1] + (tmp4 ^ tmp5 ^ tmp6)) % (uint32_t)pow(2, 32);
        i++;
    }
    return;
}

void decrypt_tea(uint32_t cipher[2], uint32_t plain[2], uint32_t key[4])
{
    // Your code here
    uint32_t sum = 0xDDE6E400;
    uint32_t tmp1;
    uint32_t tmp2;
    uint32_t tmp3;
    uint32_t tmp4;
    uint32_t tmp5;
    uint32_t tmp6;

    uint32_t delta = 0x9E3779B9;

    int i = 0;
    while (i < 1024)
    {

        tmp4 = ((cipher[0] << 4) + key[2]) % (uint32_t)pow(2, 32);
        tmp5 = (cipher[0] + sum) % (uint32_t)pow(2, 32);
        tmp6 = ((cipher[0] >> 5) + key[3]) % (uint32_t)pow(2, 32);
        cipher[1] = (cipher[1] - (tmp4 ^ tmp5 ^ tmp6)) % (uint32_t)pow(2, 32);
        tmp1 = ((cipher[1] << 4) + key[0]) % (uint32_t)pow(2, 32);
        tmp2 = (cipher[1] + sum) % (uint32_t)pow(2, 32);
        tmp3 = ((cipher[1] >> 5) + key[1]) % (uint32_t)pow(2, 32);
        cipher[0] = (cipher[0] - (tmp1 ^ tmp2 ^ tmp3)) % (uint32_t)pow(2, 32);
        sum = (sum - delta) % (uint32_t)pow(2, 32);
        i++;
    }
    plain[0] = cipher[0];
    plain[1] = cipher[1];
    return;
}

void encrypt_tea_ctr(uint64_t *plain, uint32_t key[4], uint64_t nonce, uint64_t *cipher, uint32_t num_blocks)
{
    // Your code here
    uint32_t i = 0;
    uint64_t j;

    uint64_t tmp1;
    uint32_t *tp1;

    uint32_t *plain_p;
    uint32_t *cipher_p;

    uint32_t tmp1_text[2];
    uint32_t tmp2_text[2];

    while (i < num_blocks)
    {

        j = (uint64_t)i;
        tmp1 = j ^ nonce;

        tp1 = (uint32_t *)&tmp1;

        tmp1_text[0] = tp1[0];
        tmp1_text[1] = tp1[1];

        encrypt_tea(tmp1_text, tmp2_text, key);

        plain_p = (uint32_t *)&plain[i];

        cipher_p = (uint32_t *)&cipher[i];

        cipher_p[0] = plain_p[0] ^ tmp2_text[0];
        cipher_p[1] = plain_p[1] ^ tmp2_text[1];
        i++;
    }
    return;
}

void decrypt_tea_ctr(uint64_t *cipher, uint32_t key[4], uint64_t nonce, uint64_t *plain, uint32_t num_blocks)
{
    // Your code here

    // Your code here
    uint32_t i = 0;
    uint64_t j;

    uint64_t tmp1;
    uint32_t *tp1;

    uint32_t *plain_p;
    uint32_t *cipher_p;

    uint32_t tmp1_text[2];
    uint32_t tmp2_text[2];

    while (i < num_blocks)
    {

        j = (uint64_t)i;
        tmp1 = j ^ nonce;

        tp1 = (uint32_t *)&tmp1;

        tmp1_text[0] = tp1[0];
        tmp1_text[1] = tp1[1];

        encrypt_tea(tmp1_text, tmp2_text, key);

        plain_p = (uint32_t *)&plain[i];

        cipher_p = (uint32_t *)&cipher[i];

        plain_p[0] = cipher_p[0] ^ tmp2_text[0];
        plain_p[1] = cipher_p[1] ^ tmp2_text[1];
        i++;
    }

    return;
}
