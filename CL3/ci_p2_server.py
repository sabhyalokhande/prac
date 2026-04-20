from xmlrpc.server import SimpleXMLRPCServer

class StringService:
    def concatenate(self, str1, str2):
        return str1 + str2

server = SimpleXMLRPCServer(('localhost', 5000))
server.register_instance(StringService())
print("String Concatenation Server running on port 5000...")
server.serve_forever()
