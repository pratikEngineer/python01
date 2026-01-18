# 17. If a customer buys more than 5 items, apply a 15% discount; otherwise, no discount
prices = [120, 40, 60, 80, 100, 30, 50]
total = sum(prices)
if len(prices) > 5:
    total = total - (total * 0.15)
    print(f"Total after 15% discount: {total}")
else:
    print(f"Total (no discount): {total}")