"""wap to perform different types of arithematic operation by taking 2 numbers from the user """

a= int(input("Enter a number :"))
b=int(input("Enter another number :"))

print(f"Addition of {a} and {b} is : ",a+b)
print(f"Subtraction of {a} and {b} is : ",a-b)
print(f"Multiplication of {a} and {b} is : ",a*b)

try:
    print(f"Division of {a} and {b} is : ",a/b)
    print(f"Floor division of {a} and {b} is : ",a//b)
    print(f"Modulo of {a} and {b} is : ",a%b)

except:
    print(f"Division of {a} and {b} is not possible")

print(f"Exponential of {a} and {b} is : ",a**b)