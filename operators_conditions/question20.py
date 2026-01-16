def is_odd_not_div_by_4(number):
    return number % 2 != 0 and number % 4 != 0

number = int(input("Enter a number: "))
result = is_odd_not_div_by_4(number)
print(f"Number: {number}")
print(f"Is odd and not divisible by 4: {result}")