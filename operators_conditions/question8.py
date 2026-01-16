def eligible_for_discount(age):
    return age > 60 or age < 25

age = int(input("Enter age: "))
result = eligible_for_discount(age)
print(f"Age: {age}")
print(f"Eligible for discount: {result}")