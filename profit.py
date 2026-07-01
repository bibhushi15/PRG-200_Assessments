cost_price = float(input("Enter cost price per plate: "))
selling_price = float(input("Enter selling price per plate: "))
plates_sold = float(input("Enter number of plates sold: "))
total_revenue = selling_price * plates_sold
total_cost = cost_price * plates_sold
total_profit = total_revenue - total_cost
profit_margin = (total_profit / total_revenue) * 100
print(f"Total revenue: Rs. {total_revenue:.2f}")
print(f"Total cost: Rs. {total_cost:.2f}")
print(f"Total profit: Rs. {total_profit:.2f}")
print(f"Profit margin: {profit_margin:.2f}%")