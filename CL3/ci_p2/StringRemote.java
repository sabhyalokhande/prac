import java.rmi.Remote;
import java.rmi.RemoteException;

public interface StringRemote extends Remote {
    String concatenate(String var1, String var2) throws RemoteException;
}
