import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:5000/") as proxy:
    try:
        str1 = input("Enter String 1: ")
        str2 = input("Enter String 2: ")
        result = proxy.concatenate(str1, str2)
        print("Concatenated Result:", result)
    except Exception as e:
        print("Client Error:", e)
