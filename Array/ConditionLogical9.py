items = [("Laptop", 1000), ("Milk", 50), ("Mobile", 500), ("Eggs", 30)]
electronics = ["Laptop", "Mobile", "TV", "Phone"]
result = []
for item, price in items:
    if item in electronics:
        result.append((item, price + (price * 0.05)))
    else:
        result.append((item, price + (price * 0.03)))
print("Updated prices:", result)