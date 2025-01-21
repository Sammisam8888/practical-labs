#wap to skip odd numbers in a range from user input

start=int(input("Enter the start of the range : "))
end=int(input("Enter the end of the range : "))
print("The even numbers in the given range are : ")
for i in range(start,end+1):
    if i%2==0:
        print(i,end=" ")
