# Assignment P5



`void * init_store(uint16_t branching, uint8_t n_processors);`

1. 建立树结构
2. 创建thread



`int btree_insert(uint32_t key, void * plaintext, size_t count, uint32_t encryption_key[4], uint64_t nonce, void * helper);`

1. 用TEA-CTR算法加密plaintext

## Search

1. 从root开始递归,设置cursor为现在的node
2. 用loop与它的keys进行比较，如果大于，继续loop，如果等于，返回key，如果小于则返回当前loop index作为index
3. 如果找不到，确认node是否是leaf，如果是，return false
4. 如果不是， 设置index为 loop index + 1
5. 之后进行loop，找到对应的child
6. 重复以上过程



## Insertion

- first we should check if the tree is empty
- if empty, then we create new node, then insertion the tree



