l=eval(input("Enter a list of elements: "))
d={}
j=0
for i in l:
    if i not in d:
        d[i] = 1
        
    else:
        l.pop(j)
    j += 1
print("List after removing duplicates:", l)