//wap to factorise a number

#include <stdio.h>
void primerange(int n){
    for (int i=2;i<=n;i++){
        while (n%i==0){
            printf("%d ",i);
            n/=i;
        }
    }}
void main()
{
    int n;
    printf("Enter a number :");
    scanf("%d",&n);
    primerange(n);
}