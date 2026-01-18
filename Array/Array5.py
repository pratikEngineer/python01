# 5. Count how many positive and negative numbers are in an array
arr = [-12, 20, -35, 40, -55, 60, -71, 80]
positive_count = 0
negative_count = 0
for num in arr:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
print(f"Positive numbers: {positive_count}")
print(f"Negative numbers: {negative_count}")