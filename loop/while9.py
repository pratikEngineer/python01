# 9. Print numbers from 1 to 20, but skip numbers divisible by 3 using a while loop
i = 1
while i <= 20:
    if i % 3 != 0:
        print(i, end=" ")
    i += 1
print()