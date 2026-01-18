# 4. Find the maximum and minimum numbers in the array
arr = [98, 34, 76, 21, 89, 45, 67, 102]
maximum = arr[0]
minimum = arr[0]
for num in arr:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")