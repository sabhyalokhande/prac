from xmlrpc.server import SimpleXMLRPCServer

bookings = {}

class HotelService:
    def bookRoom(self, guest_name):
        if guest_name in bookings:
            return f"Room already booked for {guest_name}"
        bookings[guest_name] = True
        return f"Room booked successfully for {guest_name}"

    def cancelBooking(self, guest_name):
        if guest_name not in bookings:
            return f"No booking found for {guest_name}"
        del bookings[guest_name]
        return f"Booking cancelled for {guest_name}"

server = SimpleXMLRPCServer(('localhost', 1099))
server.register_instance(HotelService())
print("Hotel Server is running...")
server.serve_forever()
