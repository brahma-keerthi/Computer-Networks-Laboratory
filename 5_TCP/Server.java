import java.net.*;
import java.io.*;


public class Server{
    public static void main(String args[]) throws Exception{
        ServerSocket sersoc = new ServerSocket(4000);
        System.out.println("Server Connected, Waiting for Client");
        Socket sock = sersoc.accept();
        System.out.println("Connection Successfull, Waiting for filename :)");
        InputStream istream = sock.getInputStream();
        BufferedReader readBuffer = new BufferedReader(new InputStreamReader(istream));
        String fname = readBuffer.readLine();
        OutputStream ostream = sock.getOutputStream();
        PrintWriter pwrite = new PrintWriter(ostream, true);

        try {
            BufferedReader contentRead = new BufferedReader(new FileReader(fname));
            String str;
            while ((str = contentRead.readLine()) != null ){
                pwrite.println(str);
            }
        }
        catch ( Exception e ){
            pwrite.println("File name does not exists");
        }
        finally{
            System.out.println("Closing Connection");
        }
    }
}