import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Server {

    public Server() {}

    public static void main(String[] args) {
        try {
            StringRemoteImpl obj = new StringRemoteImpl();
            Registry registry = LocateRegistry.createRegistry(6000);
            registry.rebind("StringService", obj);
            System.out.println("Server is running and ready...");
        } catch (Exception e) {
            System.out.println("Server Error: " + e.getMessage());
        }
    }
}
