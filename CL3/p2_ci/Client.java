import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class Client {

    public Client() {}

    public static void main(String[] args) {
        try {
            Scanner sc = new Scanner(System.in);
            System.out.print("Enter String 1: ");
            String str1 = sc.nextLine();
            System.out.print("Enter String 2: ");
            String str2 = sc.nextLine();

            Registry registry = LocateRegistry.getRegistry("localhost", 6000);
            StringRemote service = (StringRemote) registry.lookup("StringService");
            String result = service.concatenate(str1, str2);
            System.out.println("Concatenated Result: " + result);
            sc.close();
        } catch (Exception e) {
            System.out.println("Client Error: " + e.getMessage());
        }
    }
}
