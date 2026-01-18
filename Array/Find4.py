# 24. Find the sum of numbers at even indices
arr = [3, 7, 11, 15, 19, 23, 27, 31]
total = 0
for i in range(0, len(arr), 2):
    total += arr[i]
print(f"Sum of numbers at even indices: {total}")