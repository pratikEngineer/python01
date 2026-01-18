# 5. Print the factorial of 6 using a while loop
num = 6
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print(f"Factorial of {num}: {factorial}")