number = 12345
count = 0
temp = number
while temp > 0:
    count += 1
    temp //= 10
print(f"Number of digits in {number}: {count}")