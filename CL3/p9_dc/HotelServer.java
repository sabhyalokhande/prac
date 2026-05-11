import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.HashMap;

public class HotelServer extends UnicastRemoteObject implements HotelInterface {

    HashMap<String, Boolean> bookings;

    protected HotelServer() throws RemoteException {
        bookings = new HashMap<>();
    }

    public String bookRoom(String guestName) throws RemoteException {
        if (bookings.containsKey(guestName)) {
            return "Room already booked for " + guestName;
        }
        bookings.put(guestName, true);
        return "Room booked successfully for " + guestName;
    }

    public String cancelBooking(String guestName) throws RemoteException {
        if (!bookings.containsKey(guestName)) {
            return "No booking found for " + guestName;
        }
        bookings.remove(guestName);
        return "Booking cancelled for " + guestName;
    }

    public static void main(String[] args) {
        try {
            HotelServer server = new HotelServer();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("HotelService", server);
            System.out.println("Hotel Server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
