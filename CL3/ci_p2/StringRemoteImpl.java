import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class StringRemoteImpl extends UnicastRemoteObject implements StringRemote {

    StringRemoteImpl() throws RemoteException {}

    public String concatenate(String var1, String var2) {
        return var1 + var2;
    }
}
