
shares = 1000
buy_price = 32.87
sell_price = 33.92
commission = 0.02


amount_paid_for_stock = shares * buy_price
buy_commission = commission * amount_paid_for_stock
amount_sold_for = shares * sell_price
sell_commission = commission * amount_sold_for
total_paid = amount_paid_for_stock + buy_commission
total_received = amount_sold_for - sell_commission
net_amount = total_received - total_paid

print("Amount paid for the stock: ", amount_paid_for_stock)
print("Commission paid on the purchase of stock: ", buy_commission)
print("Amount that joe sold the stock for: ", amount_sold_for)
print("Commission paid on sale: ", sell_commission)
print("Net profit: ", net_amount)

if net_amount > 0:
    print("Joe made a profit.")
else:
    print("Joe lost money.")
