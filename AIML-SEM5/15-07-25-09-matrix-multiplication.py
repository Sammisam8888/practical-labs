r1=int(input("Enter the number of rows for matrix A: "))
c1=int(input("Enter the number of columns for matrix A: "))
r2=int(input("Enter the number of rows for matrix B: "))
c2=int(input("Enter the number of columns for matrix B: "))
if c1!=r2:
    print("Incompatible matrix dimensions for multiplication")
else:
    A=[]
    B=[]
    C=[]
    print("Enter the elements of matrix A:")
    for i in range(r1):
        row=list(map(int,input().split()))
        A.append(row)
    print("Enter the elements of matrix B:")
    for i in range(r2):
        row=list(map(int,input().split()))
        B.append(row)
    for i in range(r1):
        C.append([0]*c2)
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                C[i][j]+=A[i][k]*B[k][j]
    print("Resultant matrix :")
    for row in C:
        print(" ".join(map(str,row)))