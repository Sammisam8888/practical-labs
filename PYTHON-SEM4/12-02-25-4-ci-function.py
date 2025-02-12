"""
Q4 - define a function calculate compound interest
"""

def compoundinterest(p,r,t):
    return p*((1+r/100)**t)-p

p=float(input("Enter the Principal amount :"))
r=float(input("Enter the rate of interest :"))
t=float(input("Enter the time period (in years) :"))

print("The compound interest on the given amount is :",compoundinterest(p,r,t))
