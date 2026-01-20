prices = [120, 80, 40, 200, 300]
total = sum(prices)
if len(prices) >= 3:
    total = total - (total * 0.10)
    print(f"Total after 10% discount: {total}")
else:
    print(f"Total (no discount): {total}")