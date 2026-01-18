# 1. Print all even numbers in the array
arr = [12, 7, 25, 30, 50, 61, 82, 91]
print("Even numbers:")
for num in arr:
    if num % 2 == 0:
        print(num, end=" ")
print()