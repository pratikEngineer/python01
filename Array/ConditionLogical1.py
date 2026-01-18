# 11. If a number is divisible by 5, multiply it by 2; otherwise, add 3
arr = [10, 15, 18, 22, 35, 40, 50, 55]
result = []
for num in arr:
    if num % 5 == 0:
        result.append(num * 2)
    else:
        result.append(num + 3)
print("Result:", result)