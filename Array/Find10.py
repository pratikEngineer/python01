# 35. Find how many numbers in the array have at least two digits (10 or more)
arr = [1, 5, 10, 25, 30, 45, 50, 8, 99, 100]
count = 0
for num in arr:
    if num >= 10:
        count += 1
print(f"Count of numbers with at least two digits: {count}")