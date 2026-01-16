def is_div_by_3_and_5(number):
    return number % 3 == 0 and number % 5 == 0

number = int(input("Enter a number: "))
result = is_div_by_3_and_5(number)
print(f"Number: {number}")
print(f"Is divisible by 3 and 5: {result}")