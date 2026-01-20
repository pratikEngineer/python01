# Check if a number exists in the array or not
arr = [9, 18, 27, 36, 45, 54, 63, 72]
search = 63
exists = False
for num in arr:
    if num == search:
        exists = True
        break
print(f"{search} exists in array: {exists}")