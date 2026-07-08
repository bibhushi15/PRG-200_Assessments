paid1 = float(input("Enter amount paid by Suprima"))
paid2 = float(input("Enter amount paid by Unisha: "))
paid3 = float(input("Enter amount paid by Bibhushi: "))
total_expense = paid1 + paid2 + paid3
average = total_expense / 3
balance_for_suprima = paid1 - average
balance_for_unisha = paid2 - average
balance_for_bibhushi = paid3 - average
print(f"Total expense: Rs. {total_expense:.2f}")
print(f"Each friend should pay: Rs. {average:.2f}")
print(f"Suprima's balance: Rs. {balance_for_suprima:.2f}")
print(f"Unisha's balance: Rs. {balance_for_suprima:.2f}")
print(f"Bibhushi's balance: Rs. {balance_for_bibhushi:.2f}")
