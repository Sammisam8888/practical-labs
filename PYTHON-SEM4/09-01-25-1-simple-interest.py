#WAP TO PRINT THE SIMPLE INTEREST BY TAKING USER INPUT

p=int(input("Enter the Principal amount :"))
r=int(input("Enter the rate of interest :"))
t=int(input("Enter the time period :(in years)"))

si=(p*r*t)/100
print("The simple interest on the given amount and interest rate is : ",si)