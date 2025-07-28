//Q - perfect number 

#include <stdio.h>


void main()
{
    int n,i,c=0;
    printf("Enter a positive integer :");
    scanf("%d",&n);
    for(i=1;i<n;i++){
        if (n%i==0)
            c+=i;
    }
    if (c==n)
        printf("%d is a perfect number",n);
    else
        printf("%d is not a perfect number",n);
}