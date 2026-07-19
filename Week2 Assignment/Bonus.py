# Name:Bibhushi Karki
monthly_salary = float(input("Enter monthly basic salary: "))
deduction_percent = float(input("Enter deduction percentage: "))
dashain_bonus = monthly_salary
deduction_amount = dashain_bonus * deduction_percent / 100
Final_bonus = dashain_bonus - deduction_amount
print(f"Dashain bonus: Rs. {dashain_bonus:.2f}")
print(f"Deduction amount: Rs. {deduction_amount:.2f}")
print(f"Take-home bonus: Rs. {Final_bonus:.2f}")