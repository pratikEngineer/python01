def eligible_senior_not_new(age, is_new_customer):
    return age > 65 and not is_new_customer

age = int(input("Enter age: "))
new_customer = input("Are you a new customer? (yes/no): ").lower() == 'yes'
result = eligible_senior_not_new(age, new_customer)
print(f"Age: {age}")
print(f"New Customer: {new_customer}")
print(f"Eligible for senior discount: {result}")