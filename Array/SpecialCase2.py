# 42. Find the most frequently occurring number in the array
arr = [4, 4, 5, 6, 7, 5, 6, 6, 6, 7, 8]
frequency = {}
for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
max_freq = 0
most_frequent = None
for num, count in frequency.items():
    if count > max_freq:
        max_freq = count
        most_frequent = num
print(f"Most frequently occurring number: {most_frequent} (appears {max_freq} times)")