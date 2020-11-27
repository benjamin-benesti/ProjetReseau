import java.io.*;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;

public class ServeurEcho {

    public static void main(String[] args) throws IOException {
        ArrayList<ServerSocket> serverSockets = new ArrayList<>();
            for (int i = 0 ; i < args.length; i++)
            {
                ServerSocket serverSocket = new ServerSocket();
                serverSocket.bind(new InetSocketAddress(args[i],6000));
                serverSockets.add(serverSocket);
            }
            for (ServerSocket s: serverSockets)
            {
                Serveur serveur = new Serveur(s);
                serveur.run();
            }
    }

    private static class Serveur implements Runnable
    {
        private ServerSocket serverSocket;
        private Socket socket;
        private BufferedReader br;
        private PrintWriter pw;


        public Serveur(ServerSocket serverSocket)
        {
            this.serverSocket = serverSocket;

        }
        @Override
        public void run() {
            try {
                socket = serverSocket.accept();
                br = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                pw = new PrintWriter(new BufferedOutputStream(socket.getOutputStream()));
                String inputLine;
                while((inputLine = br.readLine()) != null)
                {
                    System.out.println("Server :"+ inputLine);
                    pw.println(inputLine);
                }
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
        }
    }



}
