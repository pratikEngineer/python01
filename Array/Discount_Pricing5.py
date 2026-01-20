prices = [120, 130, 100, 200, 50, 60]
total = sum(prices)
if total > 500:
    shipping = 0
else:
    shipping = 20
final_total = total + shipping
print(f"Total: {total}, Shipping: {shipping}, Final Total: {final_total}")