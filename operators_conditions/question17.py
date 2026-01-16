def eligible_both_discounts(age):
    return age > 60 and age < 25  # Impossible case

age = int(input("Enter age: "))
result = eligible_both_discounts(age)
print(f"Age: {age}")
print(f"Eligible for both discounts: {result}")