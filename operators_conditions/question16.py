def is_div_by_2_or_5(number):
    return number % 2 == 0 or number % 5 == 0

number = int(input("Enter a number: "))
result = is_div_by_2_or_5(number)
print(f"Number: {number}")
print(f"Is divisible by 2 or 5: {result}")