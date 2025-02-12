"""
Q2. wap to find the fibonacci term of a given number using function
"""

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
    

n=int(input("Enter a number : "))
print("The fibonacci term is : ",fibonacci(n))