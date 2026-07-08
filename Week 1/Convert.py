amount = float(input("Enter the amount"))
rate = float(input("Enter the exchange rate"))
fee_charged = float(input("Enter the service charge percent"))

converted_npr = amount * rate
fee = converted_npr * fee_charged / 100
final_amount = converted_npr - fee

print(f"Converted NPR amount: NPR {converted_npr:.2f}")
print(f"Fee charged: NPR {fee:.2f}")
print(f"Final amount received: NPR {final_amount:.2f}")

