#Find the missing number in an array containing numbers from 1 to n
arr = [1, 2, 3, 5, 6, 7, 8, 9, 10]
n = len(arr) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)
missing = expected_sum - actual_sum
print(f"Missing number: {missing}")