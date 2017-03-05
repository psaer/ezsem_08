package server;

public class Server{
    public static void main(String[] args) {
        ServerThread st=new ServerThread();
        new Thread(st).start();
    }    
}
