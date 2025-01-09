//C Programs to display prime numbers within a range

#include <stdio.h>

void primerange(){
	int a,b,i,j,c,temp;
	printf("Enter the initial value of range :");
	scanf("%d",&a);
	printf("Enter the final value of range :");
	scanf("%d",&b);
	if (a>b){
		temp=b;b=a;a=temp;}
	printf("The prime numbers in the given range is : \n");
	for (i=a;i<=b;i++){
		c=0;
		if (i<2)
			continue;
		for(j=1;j<=i;j++){
			if(i%j==0)
				c+=1;
		}
		((c==2)?printf("%d ",i):NULL);
	}
}
void main(){
	primerange();
}
