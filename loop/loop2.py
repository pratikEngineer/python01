# 2. Print the first 5 even numbers using a for loop
count = 0
for i in range(2, 100):
    if i % 2 == 0:
        print(i, end=" ")
        count += 1
        if count == 5:
            break
print()

# Alternative approach
for i in range(1, 6):
    print(i * 2, end=" ")
print()