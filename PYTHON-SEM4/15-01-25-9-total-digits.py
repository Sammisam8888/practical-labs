#wap to print titak digits in a number by taking user input

n=int(input("Enter a number : "))
count=0
while n>0:
    count+=1
    n=n//10
print("The number of digits in the given number is : ",count)
