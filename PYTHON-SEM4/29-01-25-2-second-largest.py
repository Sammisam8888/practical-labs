l=eval(input("Enter a list of integers : "))
large=l[0]
secondlarge=l[0]
for i in l:
    if i>large:
        secondlarge=large
        large=i
    elif i>secondlarge and i<large:
        secondlarge=i
    

print("The second largest element in the array is : ",secondlarge)