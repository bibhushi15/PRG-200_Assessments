def ticket_price(seat_type, count):
    if seat_type.lower() == "regular":
        price = 400
    elif seat_type.lower() == "premium":
        price = 800
    else:
        return "Invalid Input"
    total = price * count
    return total

print(f"Ticket Price: {ticket_price("premium", 10)}")
    
