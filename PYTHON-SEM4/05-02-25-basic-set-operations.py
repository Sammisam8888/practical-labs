a={2,4,True,9.4,'rahul'}
b={'yahoo',65,9.4,False}


print(type(a))

#different operations - union(|)-or, intersection(&)-and, difference(-), symmetric difference(^)-xor

c=a.union(b) #the same as c=a|b
print('a union b =',c)

d=a.intersection(b) #the same as d=a&b
print('a intersection b =',d)

e=a.difference(b) #the same as e=a-b
print('a difference b =',e)

f=a.symmetric_difference(b) #the same as f=a^b
print('a symmetric difference b =',f)
a.update(b)
# a.remove(4)
print(a)