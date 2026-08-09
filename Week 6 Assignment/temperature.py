# Name: Bibhushi Karki
import math
station_name = "Kathmandu Weather Station"
temperatures = [18.4, 22.1, 15.7, 29.3, 11.8, 25.6, 19.2]
def get_average(temps):
    return sum(temps) / len(temps)

def get_deviation(temps):
    mean = get_average(temps)   # mean is a local variable
    total = 0

    for temp in temps:
        total = total + (temp - mean) ** 2

    return math.sqrt(total / len(temps))

def get_summary(temps):
    print(station_name)
    print(f"Minimum temperature: {min(temps)}")
    print(f"Maximum temperature: {max(temps)}")
    print(f"Average temperature: {get_average(temps):.2f}")
    print(f"Standard deviation: {get_deviation(temps):.2f}")

get_summary(temperatures)
