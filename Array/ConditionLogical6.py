# 16. Given an array of product prices, apply a 10% discount on items above 100
prices = [150, 200, 50, 80, 120, 95, 300, 400]
result = []
for price in prices:
    if price > 100:
        result.append(price - (price * 0.10))
    else:
        result.append(price)
print("Prices after discount:", result)