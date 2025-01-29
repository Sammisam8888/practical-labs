l1=['ram',25.5,10,True,2+5j]
print("l1=",l1)
print("type of l1=",type(l1))
print("l1[0]",l1[0])

l1.append('shyam')
print("l1 after append =",l1)

print(l1[-1])

print(l1[-6])

l2=[1,'two',4.6]

l2.extend(l2)
print(l2)

l1.insert(2,'three')
print("l1 after insert=",l1)

l3=l2.copy()
print("l3=",l3)

l1.pop()
print("l1 after pop=",l1)
l1.remove(10)
print("l1 after remove=",l1)

