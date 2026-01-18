# 13. Replace all prime numbers in the array with -1
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

arr = [11, 22, 37, 44, 53, 61, 72, 88]
result = []
for num in arr:
    if is_prime(num):
        result.append(-1)
    else:
        result.append(num)
print("Result:", result)