n=int(input("Enter the number of rows : "))

for i in range (n):
    for j in range (n):
        if i==j or i+j==n-1 or i==0 or i==n-1:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()