print("Nested loops execution flow:")
for outer in range(1, 4):
    print(f"\nOuter loop iteration: {outer}")
    for inner in range(1, 3):
        print(f"  Inner loop iteration: {inner}")
        print(f"  Outer={outer}, Inner={inner}")