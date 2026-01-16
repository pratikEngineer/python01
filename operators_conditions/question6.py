def is_in_ranges(number):
    return (1 <= number <= 10) or (20 <= number <= 30)

number = int(input("Enter a number: "))
result = is_in_ranges(number)
print(f"Number: {number}")
print(f"Is in range [1, 10] or [20, 30]: {result}")