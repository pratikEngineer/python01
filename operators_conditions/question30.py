def is_div_by_4_or_6(number):
    return number % 4 == 0 or number % 6 == 0

number = int(input("Enter a number: "))
result = is_div_by_4_or_6(number)
print(f"Number: {number}")
print(f"Is divisible by 4 or 6: {result}")