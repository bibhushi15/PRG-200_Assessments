previous_reading = float(input("Enter the previous meter reading"))
current_reading = float(input("Enter the current reading"))
rate = float(input("Enter the rate per unit"))
service_charge = float(input("Enter fixed monthly service charge: "))
units_consumed = current_reading - previous_reading
energy_charge = units_consumed * rate
total_bill = energy_charge + service_charge
print(f"Units consumed: {units_consumed:.2f}")
print(f"Energy charge: Rs. {energy_charge:.2f}")
print(f"Service charge: Rs. {service_charge:.2f}")
print(f"Total bill: Rs. {total_bill:.2f}")
