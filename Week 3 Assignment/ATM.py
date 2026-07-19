balance = float(input("Enter your current balance: "))
daily_withdrawn = float(input("Enter amount already withdrawn today: "))
amount = float(input("Enter amount you want to withdraw: "))
daily_limit = 50000
if amount % 500 != 0:
    print("Invalid amount. Must be a multiple of NPR 500.")
elif amount > balance:
    print("Insufficient balance.")
elif daily_withdrawn + amount > daily_limit:
    print("Daily withdrawal limit reached.")
else:
    balance = balance - amount
    print("Withdrawal successful.")
    print(f"Your current balance after withdrawal: NPR {balance:.2f}")