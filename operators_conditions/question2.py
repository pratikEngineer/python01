def is_outside_range(value):
    return value < -10 or value > 10

value = int(input("Enter a value: "))
result = is_outside_range(value)
print(f"Value: {value}")
print(f"Is outside range [-10, 10]: {result}")