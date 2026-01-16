def is_multiple_of_3_and_7(number):
    return number % 3 == 0 and number % 7 == 0

number = int(input("Enter a number: "))
result = is_multiple_of_3_and_7(number)
print(f"Number: {number}")
print(f"Is multiple of 3 and 7: {result}")