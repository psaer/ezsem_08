#include <winsock2.h>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <iostream>
#include <thread>

using namespace std;

char SERVER_ADDR[15]="192.168.0.102";
//char SERVER_ADDR[15]="127.0.0.1";
int SERVER_PORT=8006;
char buf[1];
bool working=true;

HANDLE hMutex;

int sock;
//char msg[20]="Hello from client";
int readTillSeparator(char *buffer, string& rez){
    int rc=1;
    while(rc!=0){
        rc=recv(sock,buffer,1,0);
        if(rc<=0){
            return 0;
        }
        if(buffer[0]=='\n'){
            //rez=rez.substr(0,rez.size()-1);
            return 1;
        }
        rez=rez+buffer[0];
    }
}
int clientProcess(){   
    while(working){
        string tmp="";
        getline(cin,tmp);
        tmp=tmp+"\n";
        if(send(sock, tmp.c_str(), tmp.length(), 0)<0){
            puts("Send failed. Error");
            working=false;
            exit(1);
        }
    }
    return 0;
}


int main(int argc, char** argv) {
    struct sockaddr_in server;

    WSADATA wsaDATA;
    int iResult=WSAStartup(MAKEWORD(2,2), &wsaDATA);
    if(iResult!=0){
        printf("Error code: %d\n",iResult);
        exit(0);
    }

    if((sock=socket(AF_INET,SOCK_STREAM,IPPROTO_TCP))==SOCKET_ERROR){
        printf("Socket() failed with error code: %d",WSAGetLastError());
        exit(EXIT_FAILURE);
    }else
        puts("Socket created");
    
    server.sin_addr.s_addr = inet_addr(SERVER_ADDR);
    server.sin_port = htons(SERVER_PORT);
    server.sin_family = AF_INET;
    
    if (connect(sock, (struct sockaddr *)&server, sizeof(server)) < 0){
        puts("Connect failed. Error");
        exit(1);
    }else
        puts("Connected");

    CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)clientProcess, NULL, 0, NULL);

    string rez="";
    
    while(working){
        rez="";
        if(readTillSeparator(buf,rez)==1){
                    cout<<rez<<endl;
        }else{
            cout<<"You are disconnected!"<<endl;
            working=false;
        }
    }
    return (EXIT_SUCCESS);
}