exchange_rate = 158.58

def convert(USD):
    NPR = USD * exchange_rate
    print(f"converted amount: {NPR:.2f}")
    
convert(5)
convert(50)
convert(500)
convert(5000)