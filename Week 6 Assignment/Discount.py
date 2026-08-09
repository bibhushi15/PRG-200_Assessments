# Name: Bibhushi Karki
# Own Module file
TAX_RATE = 0.13

def apply_discount(price, percent):
    discount = price * percent / 100
    return price - discount

def apply_tax(price):
    tax = price * TAX_RATE
    return price + tax

def final_price(price, discount_pct):
    price_after_discount = apply_discount(price, discount_pct)
    return apply_tax(price_after_discount)