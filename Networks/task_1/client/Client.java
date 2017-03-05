package client;

import java.io.*;
import java.net.*;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Client {
    
    private static int SERVER_PORT=8090;
    private static String SERVER_IP="127.0.0.1";
    private static boolean work=true;

    public static void main(String[] args) {
        try{
            Socket echoSocket = new Socket(SERVER_IP, SERVER_PORT);
            
            PrintWriter out = new PrintWriter(echoSocket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(echoSocket.getInputStream()));
            BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));
            
            
            
            Runnable consoleReader = new Runnable() {
            @Override
                public void run() {
                    while(work){
                        try {
                            String userInput = stdIn.readLine();
                            out.println(userInput);
                        } catch (IOException ex) {
                            Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
                        }
                    }
                }
            };
            new Thread(consoleReader).start();
        
            while (work) {   
                String echo=in.readLine();
                if(echo==null){
                    work=false;  
                    System.out.println("You are disconnected.");
                }else
                    System.out.println("echo: " + echo);
            }
            echoSocket.close();           
        } catch (UnknownHostException e) {
            System.err.println("Don't know about " + SERVER_IP);
            System.exit(1);
        } catch (IOException e) {
            System.err.println("Couldn't get I/O for the connection to " + SERVER_IP);
            System.exit(1);
        } 
    }
}
