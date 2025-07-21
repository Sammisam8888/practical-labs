n=int(input("Enter a number : "))
sum =n
while(sum//10!=0):
	 s=sum
	 sum=0
	 while(s%10!=0):
	 	sum+=s%10
	 	s//=10

print(f"The single digit sum of the given integer is : {sum}")
