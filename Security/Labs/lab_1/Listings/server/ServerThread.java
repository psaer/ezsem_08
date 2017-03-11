package server;

import java.io.BufferedReader;
import java.net.ServerSocket;
import java.net.Socket;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.InetAddress;
import java.util.ArrayList;
import java.util.Map;
import java.util.Scanner;
import java.util.concurrent.ConcurrentHashMap;
import java.util.logging.Level;
import java.util.logging.Logger;

public class ServerThread implements Runnable{
    protected int           SERVER_PORT = 8090;
    protected String        SERVER_IP   = "127.0.0.1";
    
    protected ServerSocket  serverSocket = null;
    protected boolean       isStopped    = false;
       
    private ConcurrentHashMap<clientThread, String> mClients;
    
    Scanner s = new Scanner(System.in);

    public void run(){
        Runnable server = new Runnable() {
            @Override
            public void run() {
                while(!isStopped){
                    String input = s.next();
                    switch (input) {
                        case "show":
                            showClients();
                            break;
                        case "kill":
                            int id=Integer.parseInt(s.next());
                            deleteClientById(id);
                            break;
                        case "stop":
                            stop();
                            break;
                    }
                }
            }
        };
        new Thread(server).start();
        mClients = new ConcurrentHashMap<>();
        openServerSocket();

        while(!isStopped){
            Socket clientSocket = null;
            try {
                clientSocket = this.serverSocket.accept();
            } catch (IOException e) {
                System.out.println("Can't accept socket.");
                return;
            }
            addClient(clientSocket);
        }
    }

    private void addClient(Socket clientSocket){
        clientThread CT=new clientThread(clientSocket, this);
        CT.start(); 
        synchronized (mClients) {
            mClients.put(CT, "");
        }    
    }
    private synchronized void deleteClientById(int id){
        int i=1;
        for (Map.Entry<clientThread,String> entry : mClients.entrySet()) {
            clientThread key = entry.getKey();
            if(i==id){
                key.finish();
                mClients.remove(key);
                return;
            }
            i++;
        }
        System.out.println("No clients with this id");
    }
    public synchronized void removeClient(clientThread CT){
        synchronized (mClients) {
            mClients.remove(CT);
        }  
    }   
    private synchronized void showClients(){
        int i=1;
        for (Map.Entry<clientThread,String> entry : mClients.entrySet()) {
            clientThread key = entry.getKey();
            System.out.println(i+"|"+key.getAddr());
            i++;
        }
    }

    public synchronized void stop(){
        for (Map.Entry<clientThread,String> entry : mClients.entrySet()) {
            clientThread key = entry.getKey();
            key.finish();
            mClients.remove(key);
        }
        this.isStopped = true;
        try {
            this.serverSocket.close();
            System.out.println("Server stopped.");
        } catch (IOException e) {
            System.out.println("Error closing server. Error: "+e);
        }
    }

    private void openServerSocket() {
        try {
            this.serverSocket = new ServerSocket(this.SERVER_PORT,0,InetAddress.getByName(SERVER_IP));
        } catch (IOException e) {
            throw new RuntimeException("Cannot open port 8080", e);
        }
        System.out.println("Server started.") ;
    }
}
