def classify_age(age):
    if age < 13:
        return "Child"
    elif 13 <= age <= 19:
        return "Teen"
    else:
        return "Adult"

age = int(input("Enter age: "))
result = classify_age(age)
print(f"Age: {age}")
print(f"Age Group: {result}")