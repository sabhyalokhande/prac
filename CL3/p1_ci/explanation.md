# P1 — XML-RPC Factorial Service

## What is this Practical?
A client-server program where the client sends a number to the server over a network, and the server computes and returns the factorial. Communication uses **XML-RPC** — a protocol that lets programs call functions on a remote machine over HTTP using XML-encoded messages.

---

## Theory

### Client-Server Model
The client-server model is a distributed computing architecture where two programs communicate over a network. The **server** is always running and waiting for requests. The **client** initiates a connection, sends a request, waits for the response, and then disconnects. They can run on different machines or on the same machine using `localhost`.

### RPC — Remote Procedure Call
RPC is a programming technique that allows a program to call a function (procedure) on a different computer as if it were a local function. The programmer does not need to write explicit network code — the RPC framework handles:
- Serializing the function arguments into a transmittable format
- Sending them over the network
- Deserializing them on the server
- Calling the actual function
- Sending the return value back

### XML-RPC
XML-RPC is one specific implementation of RPC. It uses:
- **HTTP** as the transport protocol (same as web browsers use)
- **XML** as the format for encoding function names and arguments

A typical XML-RPC request looks like:
```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>calculate_factorial</methodName>
  <params><param><value><int>5</int></value></param></params>
</methodCall>
```
Python has built-in support for XML-RPC via `xmlrpc.server` and `xmlrpc.client`.

### Factorial
The factorial of n (written n!) is the product of all positive integers up to n.
- 0! = 1 (by definition)
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- Factorial is not defined for negative numbers.

### Port Number
A port is a logical endpoint on a machine identified by a number (0–65535). Multiple services can run on the same machine by using different ports. Port `8000` is used here. The client must know the correct port to connect to the server.

---

## Key Concepts

| Concept | Meaning |
|---|---|
| `localhost` | Refers to the current machine (IP: 127.0.0.1) |
| Port 8000 | The address the server listens on |
| XML-RPC | HTTP + XML based remote procedure call |
| `ServerProxy` | Client-side object that forwards calls to the server |
| `serve_forever()` | Keeps the server running until manually stopped |
| `rpc_paths` | Restricts server to accept requests only at a specific URL path |

---

## Code — Line by Line

### server.py

```python
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
```
Imports the built-in Python XML-RPC server classes.

```python
class RPCServer:
    def calculate_factorial(self, n):
```
Defines the class whose methods will be exposed to the client remotely.

```python
        if n < 0:
            raise ValueError("Input must be a non-negative integer.")
```
Validates input — factorial is undefined for negative numbers.

```python
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
```
Computes n! iteratively and returns the result to the caller (the client).

```python
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/api/v1/rpc_handler',)
```
Restricts server to only accept requests at this URL path. Any other path is rejected with HTTP 404.

```python
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
```
Creates the XML-RPC server bound to `localhost:8000`.

```python
    server.register_introspection_functions()
```
Enables built-in functions like `system.listMethods()` so clients can query what the server offers.

```python
    server.register_instance(RPCServer())
```
Registers the `RPCServer` object — all its methods become remotely callable.

```python
    server.serve_forever()
```
Starts an infinite loop accepting and handling requests.

---

### client.py

```python
import xmlrpc.client
```
Imports Python's built-in XML-RPC client.

```python
with xmlrpc.client.ServerProxy("http://localhost:8000/api/v1/rpc_handler") as proxy:
```
Creates a proxy object. Every method call on `proxy` is automatically serialized into XML, sent to the server via HTTP, and the response is deserialized and returned.

```python
    input_value = int(input("Enter number: "))
    result = proxy.calculate_factorial(input_value)
```
Takes user input and calls `calculate_factorial` on the **server** remotely. Looks like a local function call but actually travels over the network.

```python
    print(f"Factorial of {input_value} is: {result}")
```
Prints the result received back from the server.
