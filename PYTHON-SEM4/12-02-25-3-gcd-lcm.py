"""
Q3 - wap to find greatest common division and least common multiple of 2 given numbers
"""

from math import gcd,lcm


a=int(input("Enter a number : "))
b=int(input("Enter another number : "))

print("GCD is : ",gcd(a,b))
print("LCM is : ",lcm(a,b))
