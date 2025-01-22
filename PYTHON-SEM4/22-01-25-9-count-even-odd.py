l=eval(input("Enter a list of elements :"))
counteven=0
countodd=0

for i in range(len(l)) :
    if l[i]%2==0 :
        counteven+=1
    else :
        countodd+=1

print("The number of even elements in the list is ", counteven)
print("The number of odd elements in the list is ", countodd)
