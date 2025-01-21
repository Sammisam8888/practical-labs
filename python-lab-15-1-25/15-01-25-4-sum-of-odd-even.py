#WAP TO print sum of odd and even separately


start=int(input("Enter the start of the range : "))
end=int(input("Enter the end of the range : "))


oddsum=0
evensum=0

for i in range(start,end+1):
    if i%2!=0:
        oddsum+=i
    else:
        evensum+=i

print("Sum of odd numbers : ",oddsum)
print("Sum of even numbers : ",evensum)