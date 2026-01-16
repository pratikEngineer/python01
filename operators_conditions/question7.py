def is_negative_and_odd(number):
    return number < 0 and number % 2 != 0

number = int(input("Enter a number: "))
result = is_negative_and_odd(number)
print(f"Number: {number}")
print(f"Is negative and odd: {result}")