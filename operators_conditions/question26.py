def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_odd_or_prime(number):
    return number % 2 != 0 or is_prime(number)

number = int(input("Enter a number: "))
result = is_odd_or_prime(number)
print(f"Number: {number}")
print(f"Is odd or prime: {result}")