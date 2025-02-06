a=('ram',6.7,9)
#tuples are immutable

print(type(a))
print(len(a))
#convert tuple to a list
b=list(a)
b[0]='vssut'
#here after converting the tuple to a list, it is mutable
b.insert(90,2)

a=tuple(b)

print(a)
#now the tuple is updated after converting the new list to tuple

