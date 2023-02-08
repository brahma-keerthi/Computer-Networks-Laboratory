import java.net.*;
import java.io.*;
import java.util.Scanner;

public class Server{
    public static void main(String args[])throws Exception{
        Scanner inp =new Scanner(System.in);
        DatagramSocket sock=new DatagramSocket();
        InetAddress clientAddres=InetAddress.getByName("127.0.0.1");
        String msg;
        byte[] buffer;

        while(true){
            System.out.println("Enter the message to send>>");
            msg=inp.nextLine();
            buffer=msg.getBytes();
            DatagramPacket pack=new DatagramPacket(buffer,buffer.length,clientAddres, 4000);
            sock.send(pack);
        }
    }
}