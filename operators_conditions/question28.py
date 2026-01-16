def is_non_negative_not_div_by_7(number):
    return number >= 0 and number % 7 != 0

number = int(input("Enter a number: "))
result = is_non_negative_not_div_by_7(number)
print(f"Number: {number}")
print(f"Is non-negative and not divisible by 7: {result}")