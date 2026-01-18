# 15. Replace all odd numbers with 0 and even numbers with 1
arr = [3, 14, 27, 40, 55, 68, 71, 89]
result = []
for num in arr:
    if num % 2 == 0:
        result.append(1)
    else:
        result.append(0)
print("Result:", result)