n = int(input("Enter the size of the square matrices: "))
A = []
B = []
C = []

print("Enter the elements of matrix A:")
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter the elements of matrix B:")
for i in range(n):
    row = list(map(int, input().split()))
    B.append(row)
for i in range(n):
    C.append([0] * n)

for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

print("Resultant matrix C:")

for row in C:
    print(" ".join(map(str, row)))