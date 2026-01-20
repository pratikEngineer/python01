# Find the sum of numbers at odd indices
arr = [4, 8, 12, 16, 20, 24, 28, 32]
total = 0
for i in range(1, len(arr), 2):
    total += arr[i]
print(f"Sum of numbers at odd indices: {total}")