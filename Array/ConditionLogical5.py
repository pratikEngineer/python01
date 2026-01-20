arr = [3, 14, 27, 40, 55, 68, 71, 89]
result = []
for num in arr:
    if num % 2 == 0:
        result.append(1)
    else:
        result.append(0)
print("Result:", result)