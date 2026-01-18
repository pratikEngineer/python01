# 31. Find the count of numbers divisible by both 3 and 5
arr = [15, 30, 45, 60, 75, 90, 105, 120]
count = 0
for num in arr:
    if num % 3 == 0 and num % 5 == 0:
        count += 1
print(f"Count of numbers divisible by both 3 and 5: {count}")