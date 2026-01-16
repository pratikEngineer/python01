number = int(input("Enter a number: "))

if number < 150 or number > 950:
    print("Invalid number")
else:
    if number % 2 == 0:
        print(f"{number} is even")
        remainder = number % 4
        print(f"Remainder when divided by 4: {remainder}")
    else:
        print(f"{number} is odd")
        remainder = number % 3
        print(f"Remainder when divided by 3: {remainder}")