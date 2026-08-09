from Discount import final_price, TAX_RATE

products = [
    ("Laptop", 85000, 10),
    ("Headphones", 4500, 15),
    ("Phone Case", 800, 5),
    ("USB Cable", 600, 0),
]

print(f"Imported tax rate: {TAX_RATE}")

# Calculate final price for each product
for product in products:
    name = product[0]
    price = product[1]
    discount = product[2]

    final = final_price(price, discount)

    print(f"{name} | Original Price: NPR {price} | Final Price: NPR {final:.2f}")