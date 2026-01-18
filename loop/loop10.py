# 10. Print a specific character in a string
word = "scala"
char_to_find = "s"

if char_to_find in word:
    print(f"Character '{char_to_find}' is present in '{word}'")
    for char in word:
        if char == char_to_find:
            print(f"Found: {char}")
else:
    print(f"Character '{char_to_find}' is not present in '{word}'")