# 32. Replace all multiples of 10 with -1
arr = [10, 25, 30, 45, 50, 65, 70, 85]
result = []
for num in arr:
    if num % 10 == 0:
        result.append(-1)
    else:
        result.append(num)
print("Result:", result)