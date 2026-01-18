arr = [10, 20, 30, 40, 50, 60, 70, 80]
is_sorted = True
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break
print(f"Is array sorted in ascending order: {is_sorted}")



