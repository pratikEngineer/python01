def can_vote_or_drive(age):
    return age >= 18 or age >= 16

age = int(input("Enter age: "))
result = can_vote_or_drive(age)
print(f"Age: {age}")
print(f"Can vote or drive: {result}")