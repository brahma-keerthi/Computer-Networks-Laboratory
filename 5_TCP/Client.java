import java.net.*;
import java.io.*;

public class Client {
    public static void main(String args[]) throws Exception{
        Socket sock=new Socket("127.0.0.1",4000);
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter Filename : ");
        String fname=br.readLine();
        OutputStream oStream=sock.getOutputStream();
        PrintWriter pWrite=new PrintWriter(oStream,true);
        pWrite.println(fname);

        InputStream istream=sock.getInputStream();
        BufferedReader br2=new BufferedReader(new InputStreamReader(istream));
        String str;
        while((str=br2.readLine())!=null){
            System.out.println(str);
        }
    }
}
