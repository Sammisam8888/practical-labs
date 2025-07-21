l=eval(input("Enter the elements of a list : "))

l1=[]

for i in range (-1,-len(l)-1,-1):
	l1.append(l[i])
	
print (f"The reverse rotation of the given list is : {l1}")
	
