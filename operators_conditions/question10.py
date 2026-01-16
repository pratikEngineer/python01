def is_non_negative_or_even(number):
    return number >= 0 or number % 2 == 0

number = int(input("Enter a number: "))
result = is_non_negative_or_even(number)
print(f"Number: {number}")
print(f"Is non-negative or even: {result}")