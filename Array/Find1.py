# 21. Find the index of a given number in the array. If not found, return -1
arr = [10, 20, 30, 40, 50, 60, 70, 80]
search = 50
index = -1
for i in range(len(arr)):
    if arr[i] == search:
        index = i
        break
print(f"Index of {search}: {index}")