prices = [80, 150, 220, 90, 350, 500, 100]
result = []
for price in prices:
    if price < 100:
        result.append(price - (price * 0.05))
    elif 100 <= price <= 300:
        result.append(price - (price * 0.10))
    else:
        result.append(price - (price * 0.15))
print("Prices after tiered discount:", result)