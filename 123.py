def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def main():
    
    num1 = int(input("1st number: "))
    num2 = int(input("2nd number: "))
    operation = input("Operation: ")
    if(operation == "add"):
        print(add(num1, num2))
    elif(operation == "sub"):
        print(sub(num1, num2))
    elif(operation == "mul"):
        print(mul(num1, num2))
    elif(operation == "div"):
        print(div(num1, num2))
    else:
        print("You are gay")

main()