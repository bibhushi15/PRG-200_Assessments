def recharge_cost(gb, validity_days = 30):
    if gb == 1:
        price = 100
    elif gb == 5:
        price = 450
    elif gb == 10:
        price = 800
    else:
        "Data pacakage not available"
    print(f"price:NPR{price},Validity:{validity_days}days")
    
recharge_cost(10)