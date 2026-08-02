# Name: Bibhushi Karki
class Bus:
    def __init__(self, route, total_seats):
        self.route = route
        self.total_seats = total_seats
        self.booked = {}

    def book_seat(self, seat_number, passenger_name):
        if seat_number in self.booked:
            print(f"Seat {seat_number} already booked")
        else:
            self.booked[seat_number] = passenger_name
            print(f"Seat {seat_number} booked for {passenger_name}")

    def available_seats(self):
        return self.total_seats - len(self.booked)

    def passenger_list(self):
        print("Passenger List:")
        for seat in self.booked:
            print(f"Seat {seat}: {self.booked[seat]}")

bus = Bus("Kathmandu - Pokhara", 10)
bookings = [
    (3, "Ramila Shrestha"),
    (7, "Deepak Gurung"),
    (3, "Anita Rai"),
    (1, "Prakash Magar"),
    (7, "Suman Tamang")
]
for booking in bookings:
    bus.book_seat(booking[0], booking[1])
print(f"Available seats: {bus.available_seats()}")
bus.passenger_list()