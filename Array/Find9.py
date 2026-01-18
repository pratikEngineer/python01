# 34. Replace each number with the difference between its left and right neighbors
arr = [10, 20, 30, 40, 50, 60, 70, 80]
result = [0]  # First element has no left neighbor
for i in range(1, len(arr) - 1):
    diff = arr[i - 1] - arr[i + 1]
    result.append(diff)
result.append(0)  # Last element has no right neighbor
print("Result:", result)