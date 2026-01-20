arr = [1, 2, 3, 4, 3, 2, 1]
is_palindrome = True
n = len(arr)
for i in range(n // 2):
    if arr[i] != arr[n - 1 - i]:
        is_palindrome = False
        break
print(f"Is palindrome: {is_palindrome}")