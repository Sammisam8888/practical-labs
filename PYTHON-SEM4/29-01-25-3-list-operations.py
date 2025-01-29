l1=[57,8,67,15,30]
l2=['Ram',10,"bull",15]

print("length of l1 is : ",len(l1))
print("length of l2 is : ",len(l2))

l1.sort()

print("l1 after sorting is : ",l1)
print("Highest element in l1 is : ",l1[-1])

l3=l1[-1:-4:-1]
print("List after slicing last 3 elements : ",l3)

l2.extend(l1)
print("After adding elements of l1 to l2 : ",l2)

l1.append(25)
l1.append(98)
l1.append(90)

print("l1 after appending 25,98,90 : ",l1)
