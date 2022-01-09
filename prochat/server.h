#ifndef SERVER_H
#define SERVER_H

#define MAX_MSG 2046

struct Message{
    unsigned short type;
    unsigned char contents[MAX_MSG];
};


struct Client{
    char domain[257];
    char identifier[257];
    struct Client *next;
    
};


#endif
