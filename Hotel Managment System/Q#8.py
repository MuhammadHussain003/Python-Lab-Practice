class Room:
    def __init__(self, room_no, room_type, price_per_night):
        self.room_no = room_no
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.availability = True


class Guest:
    def __init__(self, name, guest_id):
        self.name = name
        self.guest_id = guest_id
        self.booked_rooms = []


class Booking:
    def __init__(self, booking_id, guest, room, check_in_date, check_out_date):
        self.booking_id = booking_id
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date


class Hotel:
    rooms = []
    guests = []
    bookings = []

    def add_room(self, room):
        self.rooms.append(room)
        print(f"Room No:{room.room_no} has {room.room_type} and Price per night {room.price_per_night}")

    def register_guest(self, guest):
        self.guests.append(guest)
        print(f"Guest {guest.name}  Id:{guest.guest_id} has been registered successfully")

    def make_booking(self, booking):
        self.bookings.append(booking)
        booking.room.availability = False
        booking.guest.booked_rooms.append(booking.room)
        print(
            f"Hi {booking.guest.name} your booking has been confirmed for {booking.check_in_date} to {booking.check_out_date} at Room No{booking.room.room_no}")

    def check_in_date(self, booking_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                print(f"Guest {booking.guest.name} check in  Room No{booking.room.room_no}")
                break

        return "Booking not found"

    def check_out_date(self, booking_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                booking.room.availability = True
                booking.guest.booked_rooms.remove(booking.room)
                print(f"Guest {booking.guest.name} checked out of room {booking.room.room_no}")
                break
        else:
            print("Booking not found")


room1 = Room(1, " 2 bed", 3000)
room2 = Room(2, "4 bed", 4000)
guest1 = Guest("Ahmad Ali", "GST_01")
guest2 = Guest("Khawar Nadeem", "GST-092")
booking1 = Booking("BKG-01", guest1, room1, "3-7-2023", "6-7-2003")
booking2 = Booking("BKG-2", guest2, room2, "5-7-2023", "9-7-2003")

hotel = Hotel()
hotel.add_room(room1)
hotel.add_room(room2)
hotel.register_guest(guest1)
hotel.register_guest(guest2)
hotel.make_booking(booking1)
hotel.make_booking(booking2)
hotel.check_in_date("BKG-01")
hotel.check_in_date("BKG-2")
hotel.check_out_date("BKG-2")
