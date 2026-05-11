import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class HotelClient {

    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            HotelInterface hotel = (HotelInterface) registry.lookup("HotelService");
            Scanner sc = new Scanner(System.in);

            while (true) {
                System.out.println("\n1. Book Room");
                System.out.println("2. Cancel Booking");
                System.out.println("3. Exit");
                System.out.print("Enter choice: ");
                int choice = sc.nextInt();
                sc.nextLine();

                if (choice == 1) {
                    System.out.print("Enter guest name: ");
                    String name = sc.nextLine();
                    System.out.println(hotel.bookRoom(name));
                } else if (choice == 2) {
                    System.out.print("Enter guest name: ");
                    String name = sc.nextLine();
                    System.out.println(hotel.cancelBooking(name));
                } else {
                    break;
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
