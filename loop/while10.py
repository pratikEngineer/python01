# 10. Print the square of all even numbers from 2 to 10 using a while loop
i = 2
while i <= 10:
    if i % 2 == 0:
        print(f"{i}² = {i**2}")
    i += 1