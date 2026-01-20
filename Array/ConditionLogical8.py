prices = [250, 500, 750, 300, 100, 800, 900]
result = []
for price in prices:
    if price > 500:
        result.append(0)
    else:
        result.append(price)
print("Prices after offer:", result)