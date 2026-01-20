arr = [25, 60, 45, 80, 33, 90, 10, 55]
result = []
for num in arr:
    if num > 50:
        result.append(num - (num * 0.10))
    else:
        result.append(num + (num * 0.20))
print("Result:", result)