#WAP TO PRINT THE SIMPLE INTEREST & compound interest BY TAKING USER INPUT

p=float(input("Enter the Principal amount :"))
r=float(input("Enter the rate of interest :"))
t=float(input("Enter the time period (in years) :"))

si=(p*r*t)/100
ci=p*pow((1+r/100),t)
ci-=p
print("The simple interest on the given amount is :",si)
print("The compound interest on the given amount is :",ci)