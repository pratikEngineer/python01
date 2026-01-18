# Print numbers from 1 to 10, skip 5 and 6
for i in range(1, 11):
    if i == 5 or i == 6:
        continue
    print(i, end=" ")
print()