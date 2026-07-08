for i in range(10):
    store_name = input(f"Enter store {i+1} name: ")
    units = float(input(f"Enter units consumed by {store_name}: "))
    if units <= 50:
        bill = units * 20
    elif units <= 100:
        bill = (50 * 20) + ((units - 50) * 40)
    else:
        bill = (50 * 20) + (50 * 40) + ((units - 100) * 60)
    print(f"{store_name} consumed {units} units.")
    print(f"Electric bill for {store_name} is Rs. {bill}")