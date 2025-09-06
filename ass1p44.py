
cost_price = float(input("Enter the Cost Price (CP): "))
selling_price = float(input("Enter the Selling Price (SP): "))


if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit of ₹", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss of ₹", loss)
else:
    print("No Profit, No Loss")
