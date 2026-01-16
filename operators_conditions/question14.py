def is_non_positive_and_even(number):
    return number <= 0 and number % 2 == 0

number = int(input("Enter a number: "))
result = is_non_positive_and_even(number)
print(f"Number: {number}")
print(f"Is non-positive and even: {result}")