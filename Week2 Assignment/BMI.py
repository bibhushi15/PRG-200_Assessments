# Name:Bibhushi Karki
weightinkg = float(input("Enter weight in kg: "))
heightincm = float(input("Enter height in cm: "))
heightinm = heightincm / 100
bmi = weightinkg / heightinm ** 2
print(f"Height in meters: {heightinm:.2f}")
print(f"BMI: {bmi:.1f}")