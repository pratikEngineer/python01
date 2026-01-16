def is_div_by_5_or_9(number):
    return number % 5 == 0 or number % 9 == 0

number = int(input("Enter a number: "))
result = is_div_by_5_or_9(number)
print(f"Number: {number}")
print(f"Is divisible by 5 or 9: {result}")