total = 0
count = 0
for num in range(28, 97, 2):
    total += num
    count += 1
average = total / count
print(f"Average of series (28, 30, 32, ..., 96): {average}")