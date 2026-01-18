# 20. If the total bill is above 1000, apply a flat 100 discount; otherwise, no discount
prices = [150, 200, 250, 300, 400, 50, 100]
total = sum(prices)
if total > 1000:
    total = total - 100
    print(f"Total after discount: {total}")
else:
    print(f"Total (no discount): {total}")