#Find the product of all odd numbers in the array
arr = [3, 5, 7, 9, 11, 13, 15, 17]
product = 1
for num in arr:
    if num % 2 != 0:
        product *= num
print(f"Product of all odd numbers: {product}")