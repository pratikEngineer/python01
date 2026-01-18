# Print pattern using a while loop:
# 1
# 12
# 123
# 1234
i = 1
while i <= 4:
    for j in range(1, i + 1):
        print(j, end="")
    print()
    i += 1