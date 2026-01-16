def is_positive_not_div_by_3(number):
    return number > 0 and number % 3 != 0

number = int(input("Enter a number: "))
result = is_positive_not_div_by_3(number)
print(f"Number: {number}")
print(f"Is positive and not divisible by 3: {result}")