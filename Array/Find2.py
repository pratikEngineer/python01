# 22. Find the count of numbers greater than a given threshold
arr = [15, 25, 35, 45, 55, 65, 75, 85]
threshold = int(input("Enter threshold: "))
count = 0
for num in arr:
    if num > threshold:
        count += 1
print(f"Count of numbers greater than {threshold}: {count}")