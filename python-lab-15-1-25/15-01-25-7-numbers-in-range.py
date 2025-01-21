#wap to print numbers in a range

start=int(input("Enter the start of the range : "))
end=int(input("Enter the end of the range : "))
print("The numbers in the given range are : ")
for i in range(start,end+1):
    print(i,end=" ")