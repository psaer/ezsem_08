package server;

import java.io.*;
import java.net.Socket;
import java.net.SocketAddress;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.logging.Level;
import java.util.logging.Logger;

public class clientThread extends Thread {
    protected Socket clientSocket = null;
    private SocketAddress remoteAddr = null;
    private boolean finish=false;
    private ServerThread ST;

    public clientThread(Socket clientSocket, ServerThread ST) {
        this.clientSocket = clientSocket;
        this.ST=ST;
        remoteAddr = this.clientSocket.getRemoteSocketAddress();
    }
    
    public void run() {
        try{
            System.out.println("New connection accepted from: " + remoteAddr);
            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);                   
            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            
            
            String inputLine;
            while (!finish && (inputLine = in.readLine()) != null) {
                out.println(inputLine);
            }
        }catch (IOException e) {
            ST.removeClient(this);
            System.out.println("Disconnected: " + remoteAddr +" with "+e.getMessage());
            try {
                clientSocket.close();
               // System.out.println("Socket closed.");
            } catch (IOException ex) {
                Logger.getLogger(clientThread.class.getName()).log(Level.SEVERE, null, ex);
            }
            
        }
    }
    public void finish(){   
        try{
            clientSocket.close();
        }catch(final IOException e){
            System.out.println("Can't close socket. Error: "+e.getMessage());
        }
    }
    public String getAddr(){
        return remoteAddr.toString();
    }
}