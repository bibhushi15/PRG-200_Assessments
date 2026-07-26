# Name: Bibhushi Karki
inventory = {
    "rice": {"price": 120, "stock": 20},
    "milk": {"price": 90, "stock": 10},
    "bread": {"price": 60, "stock": 15},
    "eggs": {"price": 15, "stock": 30}
}
cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}
def process_order(inventory, cart):
    total = 0
    for item in cart:
        quantity = cart[item]
        if quantity <= inventory[item]["stock"]:
            cost = inventory[item]["price"] * quantity
            total = total + cost
            inventory[item]["stock"] = inventory[item]["stock"] - quantity
            print(f"{item} x{quantity} = NPR {cost}")
        else:
            print(f"Sorry, not enough stock for {item}")
    print(f"Grand Total: NPR {total}")
    print("Updated stock:")
    for item in inventory:
        print(f"{item} = {inventory[item]['stock']}")
process_order(inventory, cart)