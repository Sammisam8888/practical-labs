"""Q1. create a calculator, take 2 values and user will input the operation they want to perform
+ - * / % ^
"""

def calculator(a,b,op):
    if op=='/':
        return f"The quoteint of both the numbers is : {a/b if b!=0 else "division by 0 not possible"}"
    elif op=='+':
        return f"The sum of both the numbers is : {a+b}"
    elif op=='-':
        return f"The difference of both the numbers is : {a-b}"
    elif op=='*':
        return f"The product of both the numbers is : {a*b}"
    elif op=='%':
        return f"The modular division of both the numbers is : {int(a)%int(b)}"
    elif op=='^':
        return f"The exponentiation of both the numbers is : {a**b}"
    else :
        return "Invalid,  operationcannot be performed"
    

a=float(input("Enter a number : "))
b=float(input("Enter another number : "))

op=input("Enter the exact operation you want to perform : Multiplication(*), Addition(+), Subtraction(-),Division(/),Modular division (%),Exponentiation(^) : ")

print(calculator(a,b,op))
