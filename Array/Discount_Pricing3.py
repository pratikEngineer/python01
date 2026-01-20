prices = [100, 150, 200, 250, 300, 350]
prices_sorted = sorted(prices)
total = sum(prices)
# For every 3 items, subtract the cheapest one
free_items = len(prices) // 3
for i in range(free_items):
    total -= prices_sorted[i]
print(f"Total after Buy 2 Get 1 Free: {total}")