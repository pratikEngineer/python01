string = "code"
reversed_string = ""
i = len(string) - 1
while i >= 0:
    reversed_string += string[i]
    i -= 1
print(f"Original: {string}")
print(f"Reversed: {reversed_string}")