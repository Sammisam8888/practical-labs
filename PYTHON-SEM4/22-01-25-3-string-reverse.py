s=input("Enter a string : ")
rev=""
for i in range(-1,-len(s)-1,-1):
    rev+=s[i]

print("The reverse of the string is : ",rev)