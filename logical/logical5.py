score = int(input("Enter score: "))

if 0 <= score <= 100:
    if 90 <= score <= 100:
        print("Genius")
    elif 80 <= score <= 89:
        print("Excellent")
    elif 70 <= score <= 79:
        print("Very Good")
    elif 60 <= score <= 69:
        print("Good")
    elif 40 <= score <= 59:
        print("Average")
    else:
        print("Fail")
else:
    print("Invalid input")