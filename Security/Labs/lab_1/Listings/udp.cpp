#include <winsock2.h>
#include <fstream>

#define SERVER "192.168.56.2"
#define PORT 8005

using namespace std;

int clientSocket;
sockaddr_in si_server;
int slen=sizeof(si_server);

int main(int argc, char** argv) {
    WSADATA wsa;
    
    if(WSAStartup(MAKEWORD(2,2),&wsa)!=0){
        printf("Failed WSAS initialize. Error code :%d",
        	WSAGetLastError());
        exit(EXIT_FAILURE);
    }
    
    if((clientSocket=socket(AF_INET,SOCK_DGRAM,IPPROTO_UDP))==
    	SOCKET_ERROR){
        printf("Socket() failed with error code: %d",
        	WSAGetLastError());
        exit(EXIT_FAILURE);
    }
    
    memset((char *)&si_server,0,sizeof(si_server));
    si_server.sin_family=AF_INET;
    si_server.sin_port=htons(PORT);
    si_server.sin_addr.S_un.S_addr=inet_addr(SERVER);
    
    string rez="testData";
    sendto(clientSocket,rez.c_str(),strlen(rez.c_str()), 0,
    	(struct sockaddr *)&si_server,slen);   

    return 0;
}