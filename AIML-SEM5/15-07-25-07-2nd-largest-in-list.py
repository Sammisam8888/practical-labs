l=eval(input("Enter the elements of a list : "))
mx=l[0]
mx2=l[0]
for i in l:
	if i>mx:
		mx2=mx
		mx=i
	elif i>mx2:
		mx2=i
print(f"The second largest element in the list is : {mx2}")
print(type(l[0]))
