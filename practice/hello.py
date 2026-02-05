print("hello world")


a=int(input("Enter a number: "))
b=int(input("Enter another number: "))

def add(a:int,b:int):
    return a+b

result=(add(a,b))
print(f"The sum of {a} and {b} is {result}")