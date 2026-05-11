# P9 — Hotel Booking Service (Java RMI)

## What is this Practical?
A distributed hotel room booking system using **Java RMI**. The server maintains a booking registry in memory. The client connects remotely and can book or cancel rooms by name. This demonstrates a real-world use case of distributed computing — a service running on one machine used by clients on other machines.

---

## Theory

### Distributed Systems
A distributed system is a collection of independent computers that appear to the user as a single coherent system. Key properties:
- **Transparency** — users don't know (or care) where services run
- **Scalability** — more machines can be added to handle more load
- **Fault tolerance** — if one machine fails, others continue
- **Concurrency** — multiple clients can use the system simultaneously

### Java RMI — Remote Method Invocation
RMI is Java's built-in mechanism for distributed object communication. It allows a Java program on one machine to call methods on a Java object running on a different machine — **as if it were a local object**.

#### RMI Architecture — 3 Layers

| Layer | Role |
|---|---|
| **Stub** (client side) | Proxy object that intercepts method calls and sends them over network |
| **Remote Reference Layer** | Manages the connection and handles retransmission |
| **Transport Layer** | TCP/IP socket communication |

#### RMI Communication Flow
```
Client                                    Server
  |                                          |
  | hotel.bookRoom("Alice")                  |
  |         ↓                                |
  |      [Stub]                              |
  |    serializes args                       |
  |    sends over TCP ------------------->   |
  |                                    [Skeleton]
  |                                   deserializes
  |                                   calls actual method
  |                                   serializes result
  |   <-------------------------------- sends back
  |    deserializes result                   |
  |    returns to caller                     |
  | "Room booked for Alice"                  |
```

### RMI Registry
The RMI Registry is a **name service** (like DNS for services). It runs on a specific port and maintains a map of `name → remote object`:
- Server calls `registry.rebind("HotelService", obj)` to publish the service
- Client calls `registry.lookup("HotelService")` to get a stub
- Without the registry, clients have no way to find the server object

### Remote Interface — The Contract
A remote interface defines exactly which methods clients can call remotely. It must:
- Extend `java.rmi.Remote`
- Declare every remote method with `throws RemoteException`

`RemoteException` covers network-level failures: connection refused, server crashed, network timeout, serialization errors, etc.

### UnicastRemoteObject
This base class handles all the networking infrastructure:
- **Exports** the object — makes it accessible from the network
- Creates a **server socket** to listen for incoming calls
- Manages a **thread pool** for handling multiple simultaneous clients
- Handles **marshalling/unmarshalling** (serialization of arguments and return values)

### Serialization in RMI
When a remote method is called:
1. Arguments are **serialized** (converted to byte stream) on the client
2. Bytes travel over TCP/IP to the server
3. Arguments are **deserialized** (reconstructed) on the server
4. The method runs locally on the server
5. The return value is serialized and sent back
6. Client deserializes and receives the result

`String` is serializable by default in Java, so our string concatenation/booking names work seamlessly.

### Port 1099
Port 1099 is the **default RMI registry port**. `LocateRegistry.createRegistry(1099)` starts the registry on this port. The client uses `LocateRegistry.getRegistry("localhost", 1099)` to connect to it.

---

## Key Concepts

| Concept | Meaning |
|---|---|
| Remote Interface | Defines methods callable over the network |
| Stub | Client-side proxy — forwards calls to actual remote object |
| RMI Registry | Name service — maps service names to remote objects |
| `UnicastRemoteObject` | Base class that exports an object for remote access |
| `RemoteException` | Exception for any network/RMI failure |
| `rebind` | Registers object in registry (overwrites if name exists) |
| `lookup` | Retrieves stub from registry by name |
| Port 1099 | Default RMI registry port |
| `HashMap` | In-memory data store for bookings (guest → booked) |

---

## Code — Line by Line

### HotelInterface.java

```java
public interface HotelInterface extends Remote {
```
The remote interface. Must extend `Remote` to be usable as an RMI interface.

```java
    String bookRoom(String guestName) throws RemoteException;
    String cancelBooking(String guestName) throws RemoteException;
```
The two remotely callable methods. Both declare `throws RemoteException` — network issues can occur at any time.

---

### HotelServer.java

```java
public class HotelServer extends UnicastRemoteObject implements HotelInterface {
```
Implementation class. Extends `UnicastRemoteObject` for network access. Implements `HotelInterface` to provide both methods.

```java
    HashMap<String, Boolean> bookings;
```
In-memory booking store. Acts as the database — guest names mapped to their booking status.

```java
    protected HotelServer() throws RemoteException {
        bookings = new HashMap<>();
    }
```
Constructor initializes empty booking map. Declares `throws RemoteException` because `UnicastRemoteObject`'s constructor requires it.

```java
    public String bookRoom(String guestName) throws RemoteException {
        if (bookings.containsKey(guestName)) {
            return "Room already booked for " + guestName;
        }
        bookings.put(guestName, true);
        return "Room booked successfully for " + guestName;
    }
```
Checks for duplicate bookings. If none, adds to HashMap and confirms. The response string travels back to the client over RMI.

```java
    public String cancelBooking(String guestName) throws RemoteException {
        if (!bookings.containsKey(guestName)) {
            return "No booking found for " + guestName;
        }
        bookings.remove(guestName);
        return "Booking cancelled for " + guestName;
    }
```
Validates that a booking exists before cancelling. Removes from HashMap and confirms.

```java
    Registry registry = LocateRegistry.createRegistry(1099);
    registry.rebind("HotelService", server);
```
Starts the RMI registry on port 1099 and publishes the server object under the name `"HotelService"`.

---

### HotelClient.java

```java
Registry registry = LocateRegistry.getRegistry("localhost", 1099);
HotelInterface hotel = (HotelInterface) registry.lookup("HotelService");
```
Connects to the RMI registry and retrieves the stub. `hotel` now looks like a local `HotelInterface` object — but every method call travels to the server.

```java
int choice = sc.nextInt();
```
Reads menu choice. The loop continues until choice 3 (exit).

```java
System.out.println(hotel.bookRoom(name));
```
Remote call — executes on the server, result returned and printed here.
