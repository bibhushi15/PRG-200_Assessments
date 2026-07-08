number = 1245
count = 3

for i in range(count):
    pin = int(input("Enter the pin: "))
    
    if pin == number:
        print("Enter the amount")
        break
    else:
        print("Invalid pin")
        
        if i == count - 1:
            print("Card blocked")