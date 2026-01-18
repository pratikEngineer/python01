arr = [1, 0, 2, 3, 0, 4, 0, 5, 6, 0]
result = []
zero_count = 0
for num in arr:
    if num != 0:
        result.append(num)
    else:
        zero_count += 1
for i in range(zero_count):
    result.append(0)
print("Array after moving zeros:", result)