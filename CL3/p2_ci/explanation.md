# P2 — RMI String Concatenation (Java)

## What is this Practical?
A client-server program where the client sends two strings to the server, and the server concatenates and returns them. Communication uses **Java RMI (Remote Method Invocation)** — Java's native mechanism for calling methods on objects running in a different JVM, possibly on a different machine.

---

## Theory

### Distributed Computing
Distributed computing means multiple computers working together over a network to solve a problem. Each machine runs part of the program. Key challenges are: how do they communicate? How does one machine call a function on another?

### RMI — Remote Method Invocation
RMI is Java's answer to the RPC problem. It allows a Java object on one machine (the client) to call methods on a Java object running on another machine (the server) — as if it were a local object. The programmer writes almost the same code as for local method calls.

#### How RMI Works Internally:
1. The server creates a remote object and **registers** it in the RMI Registry under a name.
2. The client **looks up** that name in the registry and receives a **stub**.
3. The stub is a local proxy — calling a method on it sends the call over the network.
4. The server receives it via a **skeleton**, invokes the actual method, and sends the result back.

```
Client                  Network                 Server
  |                        |                       |
  |-- stub.concatenate() ->|-- (serialized call) ->|
  |                        |                       |-- actual method runs
  |<- (serialized result) -|<----- result ---------|
  |                        |                       |
```

### RMI Registry
The RMI Registry is like a telephone directory. The server registers its object under a name (e.g., `"StringService"`). The client queries the registry with that name and gets a stub back. The registry runs on a specific port (6000 here).

### Remote Interface
A remote interface defines the **contract** — which methods clients are allowed to call remotely. It must extend `java.rmi.Remote`. Any method in a remote interface must declare `throws RemoteException` because network calls can always fail (connection dropped, server down, etc.).

### UnicastRemoteObject
This is the base class for remote server objects. It handles all the low-level networking:
- Exports the object so it can receive remote calls
- Manages threads for handling multiple simultaneous client connections
- Handles serialization/deserialization of arguments and return values

### Serialization
When a method is called remotely, its arguments must be converted to bytes to travel over the network — this is called **serialization**. The return value is serialized back. In Java, objects must implement `Serializable` to be passed over RMI. Primitive types (int, String) are serializable by default.

---

## Key Concepts

| Concept | Meaning |
|---|---|
| Remote Interface | Defines which methods can be called remotely |
| Stub | Client-side proxy that forwards calls to the server |
| RMI Registry | Lookup service for finding remote objects by name |
| `UnicastRemoteObject` | Makes a Java object accessible over the network |
| `RemoteException` | Exception thrown when a network/RMI error occurs |
| `rebind` | Registers (or replaces) an object in the registry |
| `lookup` | Retrieves a stub from the registry by name |
| Port 6000 | The port where the RMI registry runs in this program |

---

## Code — Line by Line

### StringRemote.java

```java
public interface StringRemote extends Remote {
```
Declares the remote interface. Extending `Remote` marks it as remotely callable.

```java
    String concatenate(String var1, String var2) throws RemoteException;
```
The only remotely callable method. Must throw `RemoteException` — required for all remote methods to handle network failures.

---

### StringRemoteImpl.java

```java
public class StringRemoteImpl extends UnicastRemoteObject implements StringRemote {
```
The actual implementation class. Extends `UnicastRemoteObject` to handle all networking automatically. Implements `StringRemote` to fulfil the contract.

```java
    StringRemoteImpl() throws RemoteException {}
```
Constructor must declare `throws RemoteException` because `UnicastRemoteObject`'s constructor can throw it during export.

```java
    public String concatenate(String var1, String var2) {
        return var1 + var2;
    }
```
Simple string join — this runs on the server when called remotely.

---

### Server.java

```java
StringRemoteImpl obj = new StringRemoteImpl();
```
Creates the remote object instance that will serve all client requests.

```java
Registry registry = LocateRegistry.createRegistry(6000);
```
Starts the RMI Registry on port 6000. Without this, clients cannot look up the service.

```java
registry.rebind("StringService", obj);
```
Publishes the object in the registry under the name `"StringService"`. Clients will use this exact name to find it.

---

### Client.java

```java
Registry registry = LocateRegistry.getRegistry("localhost", 6000);
```
Connects to the RMI Registry running on `localhost` port 6000.

```java
StringRemote service = (StringRemote) registry.lookup("StringService");
```
Retrieves the stub for `"StringService"`. The stub looks like a `StringRemote` object locally, but every method call is forwarded to the server.

```java
String result = service.concatenate(str1, str2);
```
Looks like a local method call — but actually travels over the network to the server, executes there, and the result is returned here.
