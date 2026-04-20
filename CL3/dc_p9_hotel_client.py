import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:1099/") as hotel:
    while True:
        print("\n1. Book Room")
        print("2. Cancel Booking")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter guest name: ")
            print(hotel.bookRoom(name))
        elif choice == "2":
            name = input("Enter guest name: ")
            print(hotel.cancelBooking(name))
        elif choice == "3":
            break
        else:
            print("Invalid choice")
