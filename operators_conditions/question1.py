def is_even_and_positive(number):
    return number > 0 and number % 2 == 0

number = int(input("Enter a number: "))
result = is_even_and_positive(number)
print(f"Number: {number}")
print(f"Is even and positive: {result}")