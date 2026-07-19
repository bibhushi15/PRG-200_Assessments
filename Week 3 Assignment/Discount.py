purchase_amount = float(input("Enter total purchase amount: "))
loyalty_member = input("Are you a loyalty member? yes/no: ")
if purchase_amount < 1000:
    discount_percent = 0
elif purchase_amount <= 4999:
    discount_percent = 5
elif purchase_amount <= 14999:
    discount_percent = 10
else:
    discount_percent = 20
discount_amount = purchase_amount * discount_percent / 100
amount_after_discount = purchase_amount - discount_amount
if loyalty_member == "yes":
    loyalty_discount = amount_after_discount * 5 / 100
else:
    loyalty_discount = 0
final_amount = amount_after_discount - loyalty_discount
print(f"Original amount: NPR {purchase_amount:.2f}")
print(f"Main discount: NPR {discount_amount:.2f}")
print(f"Loyalty discount: NPR {loyalty_discount:.2f}")
print(f"Final payable amount: NPR {final_amount:.2f}")