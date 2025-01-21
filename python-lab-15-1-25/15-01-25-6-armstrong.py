#wap to check whether a number is armstrong

n=int(input("Enter a number : "))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10

if sum==n:
    print("The given number is an armstrong number")
else:
    print("The given number is not an armstrong number")