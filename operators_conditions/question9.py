def is_div_by_5_and_7(number):
    return number % 5 == 0 and number % 7 == 0

number = int(input("Enter a number: "))
result = is_div_by_5_and_7(number)
print(f"Number: {number}")
print(f"Is divisible by 5 and 7: {result}")