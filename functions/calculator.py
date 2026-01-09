# simple calculator using functions in python
def addition(a,b):
    return a+b
def substraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b == 0:
        print("invalid value, please enter again")
    return a/b
def calc():
    print("select operation:")
    print("1. addition")
    print("2. substraction")
    print("3. multiplication")
    print("4. division")
    print("5. exit")
while True:
    calc()
    choice  = input("enter your choice(1/2/3/4/5):")
    if choice in('1','2','3','4'):
        try:
            num1 = float(input("enter first number:"))
            num2 = float(input("enter second number:"))
        except ValueError:
            print("invalid value! please try again..")
            continue
        if choice == '1':
            print(addition(num1,num2))
        elif choice  == '2':
            print(substraction(num1,num2))
        elif choice == '3':
            print(multiplication(num1,num2))
        elif choice == '4':
            print(division(num1,num2))
    elif choice == '5':
            print("exiting calculator")
            break
    else:
        print("invalid choice! please try again later")




