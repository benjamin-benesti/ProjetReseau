import java.io.*;
import java.net.InetAddress;
import java.net.Socket;
import java.util.Scanner;

public class ClientEcho {

    public static void main(String[] args) throws IOException {
        InetAddress inetSocketAddress = InetAddress.getByName(args[0]);
        Socket socket = new Socket(inetSocketAddress,6000);
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        PrintWriter printWriter = new PrintWriter(socket.getOutputStream());
        Scanner scanner = new Scanner(System.in);
        while(true)
        {
            System.out.println("Enter text");
            String inputLine = scanner.nextLine();
            if (inputLine.equals("exit"))
                break;
            printWriter.println(inputLine);
            String response = bufferedReader.readLine();
            System.out.println("Server response: "+response);
        }

    }
}
