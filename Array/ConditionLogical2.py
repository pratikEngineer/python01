# 12. If a number is greater than 50, reduce it by 10%; otherwise, increase it by 20%
arr = [25, 60, 45, 80, 33, 90, 10, 55]
result = []
for num in arr:
    if num > 50:
        result.append(num - (num * 0.10))
    else:
        result.append(num + (num * 0.20))
print("Result:", result)