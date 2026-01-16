def is_div_by_3_or_8(number):
    return number % 3 == 0 or number % 8 == 0

number = int(input("Enter a number: "))
result = is_div_by_3_or_8(number)
print(f"Number: {number}")
print(f"Is divisible by 3 or 8: {result}")