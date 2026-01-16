def eligible_student_or_trial(age, has_free_trial):
    return age < 25 or has_free_trial

age = int(input("Enter age: "))
free_trial = input("Do you have a free trial? (yes/no): ").lower() == 'yes'
result = eligible_student_or_trial(age, free_trial)
print(f"Age: {age}")
print(f"Free Trial: {free_trial}")
print(f"Eligible for student discount or free trial: {result}")