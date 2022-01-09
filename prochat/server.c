#include "server.h"
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <dirent.h>
#include <sys/wait.h>
#include <signal.h>

#define BUF_SIZE 2048
#define TYPE 2
#define N 256


void Child_handler(char *identifier, char *domain){

    //创建子进程

    pid_t pid = fork();

    //创建失败，直接返回

    if(pid < 0){
        
        perror("unable to fork\n");

        return;
    
    }else if(pid == 0){

        //子进程


        //创建domain
        mkdir(domain, 0666);

        //WR管道
        char client_to_handler[600];
        //RD管道
        char handler_to_client[600];
        //WR文件名
        char WR_filename[300];
        //RD文件名
        char RD_filename[300];


        strcpy(WR_filename, identifier);
        strcat(WR_filename, "_WR");



        strcpy(RD_filename, identifier);
        strcat(RD_filename, "_RD");


        strcpy(client_to_handler, domain);
        strcat(client_to_handler, "/");
        strcat(client_to_handler, identifier);
        strcat(client_to_handler, "_WR");


        strcpy(handler_to_client, domain);
        strcat(handler_to_client, "/");
        strcat(handler_to_client, identifier);
        strcat(handler_to_client, "_RD");


        

        if(mkfifo(client_to_handler, 0666) < 0){
            exit(0);
        };

        if(mkfifo(handler_to_client, 0666) < 0){
            exit(0);
        }
            
        
        //循环打开和关闭管道，读取/写入数据
        int fd;

        while(1){

            //fprintf(stderr, "pid: %d, identifier: %s, open\n", getpid(), identifier);



            fd = open(client_to_handler, O_RDONLY);

           

            
            // //打开失败，则结束子进程，返回到main
            // if(fd <= 0) {

            //     fprintf(stderr, "cannot open fd\n");

            //     close(fd);

            //     //use kill

            //     exit(0);

            // }

           

            //建立缓冲区
            char msg[BUF_SIZE];


            //读取数据
            int msg_status = read(fd, msg, sizeof(char) * BUF_SIZE);

            //关闭管道
            close(fd);

            //fprintf(stderr, "close %s\n", client_to_handler);
            
            if(msg_status == -1){
                
                fprintf(stderr, "cannot open file");

                continue;
            }

            char type[2];
        

            memset(type, '\0', 2);

            strncpy(type, msg, 2);


            
            //fprintf(stderr, "pid: %d, identifier: %s, type: %d, msg: %s\n", getpid(), identifier, type[0], msg+2);

            

            if(type[0] == 1){

                //say

                char say_msg[1790];
                char new_msg[BUF_SIZE];
                char target[600];

                //get say message
                strncpy(say_msg, msg+2, 1790);

                //create directory pointer
                struct dirent *pDirent;
                DIR *pDir;
                

                pDir = opendir(domain);

                if(pDir == NULL){

                    perror("cannot open directory");

                    continue;
                }

                 while ((pDirent = readdir(pDir)) != NULL) {


                    char *file_type = &pDirent->d_name[strlen(pDirent->d_name)- 2];

                    if(strcmp(file_type, "WR") == 0 && strcmp(pDirent->d_name, WR_filename) != 0){

                        //open fd2

                        

                        memset(target, '\0', 600);

                        strcpy(target, domain);
                        strcat(target, "/");
                        strcat(target, pDirent->d_name);

                        
                        
                        fd = open(target, O_WRONLY);

                        //fprintf(stderr, "target : %s\n", target);

                        if(fd <= 0) {

                            perror("cannot open target pipe");

                            break;

                        }

                        //change msg type
                        type[0] = 3;

                        //set identifier and message
                        strncpy(new_msg, type, 2);
                        strncpy(new_msg+2, identifier, 256);
                        strncpy(new_msg+258, say_msg, 1790);


                        write(fd, new_msg, sizeof(char) * BUF_SIZE);

                        close(fd);

                    }
                    
                    
                }
               
            }
            else if(type[0] == 2){

                char say_msg[1790];
                char new_msg[BUF_SIZE];
                char target[600];


                //get say message (except for last char)
                strncpy(say_msg, msg+2, 1789);

                //get termination

                
                say_msg[1789] = msg[2047];

               

                
                //create directory pointer
                struct dirent *pDirent;
                DIR *pDir;
                

                pDir = opendir(domain);

                if(pDir == NULL){

                    perror("cannot open directory");

                    continue;
                }

                 while ((pDirent = readdir(pDir)) != NULL) {


                    char *file_type = &pDirent->d_name[strlen(pDirent->d_name)- 2];

                    if(strcmp(file_type, "WR") == 0 && strcmp(pDirent->d_name, WR_filename) != 0){

                    
                        memset(target, '\0', 600);

                        strcpy(target, domain);
                        strcat(target, "/");
                        strcat(target, pDirent->d_name);

                        //change msg type
                        type[0] = 4;

                        //set identifier and message
                        strncpy(new_msg, type, 2);
                        strncpy(new_msg+2, identifier, 256);
                        strncpy(new_msg+258, say_msg, 1790);

                        new_msg[2047] = say_msg[1789];


                        //不知道需不需要打开

                        
                        fd = open(target, O_RDWR);  

                        if(fd <= 0) {

                            perror("cannot open target pipe");

                            break;

                        }

                        write(fd, new_msg, sizeof(char) * BUF_SIZE);

                        close(fd);

                    }                  
                }


            }
            else if(type[0] == 3){

                //recieve
                
                //create directory pointer
                struct dirent *pDirent;
                DIR *pDir;

                pDir = opendir(domain);

                if(pDir == NULL){

                    perror("cannot open directory");

                    continue;
                }
                
                
                 while ((pDirent = readdir(pDir)) != NULL) {
                    
                   
                     
                    if(strcmp(pDirent->d_name, RD_filename) == 0){

                        //open fd2
                        
                        fd = open(handler_to_client, O_WRONLY);

                        

                        if(fd <= 0) {

                            perror("cannot open child pipe");

                            break;

                        }
                       

                        write(fd, msg, sizeof(char) * BUF_SIZE);



                        close(fd);

                    }
                    
                    
                }




            }
            else if(type[0] == 4){
                //recieve con

                
                
                fd = open(handler_to_client, O_WRONLY);

                

                if(fd <= 0) {

                    perror("cannot open child pipe");

                    break;

                }

                //如果client打开这个管道并读取数据，则继续



                
                write(fd, msg, sizeof(char) * BUF_SIZE);

                close(fd);
    

            }
            else if(type[0] == 7){

                unlink(client_to_handler);
                unlink(handler_to_client);

                kill(getppid(), SIGUSR1);

                break;
                        
            }
            else{
                continue;
            }

            
        

        }


        exit(0);
    
    }else{
        //父进程直接返回到main函数

        
        return; 
        
    }
}

struct Client* add_client(struct Client *head, char *identifier, char *domain){

    struct Client *new_client = malloc(sizeof(struct Client));
    new_client->next = head;
    memset(new_client->domain, '\0', 257);
    memset(new_client->identifier, '\0', 257);

    strcpy(new_client->domain, domain);
    strcpy(new_client->identifier, identifier);
    return new_client;
    
}

int check_client(struct Client *head, char *identifier, char *domain){

    int i = 0;

    struct Client *cursor = head;

    while(cursor != NULL){

        int j = strcmp(cursor->domain, domain);
        int k = strcmp(cursor->identifier, identifier);

        if(j == 0 && k == 0){

            return i;
        }
        cursor = cursor->next;
        i = i + 1;

    }
    cursor = NULL;
    return -1;

}

int client_size(struct Client *head){

    int i = 0;
    struct Client *cursor = head;

    while(cursor != NULL){

        cursor = cursor->next;
        i = i + 1;
    }
    cursor = NULL;
    return i;
}

void delete_client(struct Client *head, char *identifier, char *domain){

    int index = check_client(head, identifier, domain);
    struct Client *cursor;

    if(index == 0){

        cursor = head->next;
        free(head);
        head = cursor;
        cursor = NULL;
    }

    //find previous node of the client
    int i = 0;
    cursor = head;
    while(cursor != NULL){

        if(i == index - 1){

            struct Client *client = cursor->next;
            struct Client *tmp = client->next;

            free(client);

            cursor->next = tmp;

            client = NULL;
            tmp = NULL;
        }
        cursor = cursor->next;
        i = i + 1;
    }
        
}

void delete_all(struct Client*head){

    struct Client *p;
    for ( ; head != NULL; head = p ) {
    p = head->next;
    free(head);
}
}

void print_client(struct Client *head){

    struct Client *cursor = head;
    while(cursor != NULL){
        fprintf(stderr, "domain: %s, identifier: %s\n", cursor->domain, cursor->identifier);
        cursor = cursor->next;
    }
}

void global_handler(int sig){

    while(wait(NULL) > 0){
        //handle
    }
}



int main(int argc, char** argv) {
    // Your code here
    
    //建立public管道
    const char *gevent = "gevent";


    //建立失败
    if(mkfifo(gevent, 0666) < 0){

        fprintf(stderr, "unable to create gevent pipe\n");
        
        return 0;
    }

    signal(SIGUSR1, global_handler);


    //建立成功，循环打开和关闭public管道
    while(1){
        
        
        //打开public管道（只读模式）
        int listen_fd = open(gevent, O_RDONLY);

        //打开失败
        if(listen_fd <= 0){

            perror("unable to create file descriptor");

            break;
        }

        //打开成功

        

        //建立缓冲区
        char buf[BUF_SIZE];

        //从管道读取数据
        int status = read(listen_fd, buf, sizeof(char) * BUF_SIZE);


        //读取失败，关闭管道，继续循环
        if(status == -1){

            close(listen_fd);

            continue;
        }

        //读取成功，关闭管道

        close(listen_fd);


        //读取type,domain,identifier

        char type[3];
        char identifier[257];
        char domain[257];

        strncpy(type, buf, 2);
        strncpy(identifier, (buf + 2), 256);
        strncpy(domain, (buf + 258), 256);

        type[2] = '\0';
        identifier[256] = '\0';
        domain[256] = '\0';

        
        //如果不连接，则继续循环
        if(!(type[0] == 0 && type[1] == 0)){  


            perror("type is not used to create pipe");

            continue;
        }

        //成功，创建child handler
        Child_handler(identifier, domain);

    }
    while(wait(NULL) > 0){
        //handle
    }


    return 0;
    
}
