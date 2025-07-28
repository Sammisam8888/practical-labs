//Q - binary search

#include <stdio.h>


void main()
{
    int a[]={5,10,15,20,25,30,35,40,45,50};
    //the first step to searching is to sort
    int k,g=0;
    printf("Enter the number to be searched :");
    scanf("%d",&k);
    int l=0,u=9,m;
    while(l<=u){
        m=(l+u)/2;
        if (k<a[m])
            u=m-1;
        else if (k>a[m])
            l=m+1;
        else {
            g=1;
            break;}
    }
    if (g==1)
        printf("the number %d is present in array at %d position",k,m+1);
    else 
         printf("the number %d is not present in array",k);    
}