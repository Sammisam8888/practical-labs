//Q - amicable number
/*
Amicable numbers are found in pairs. A given pair of numbers is Amicable if the sum of the proper divisors (not including itself) of one number is equal to the other number and vice – versa.
For example 220 & 284 are amicable numbers	First we find the proper divisors of 220:	220:1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110
1+ 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284	Now, 284:
1, 2, 4, 71, 142	1 + 2 + 4 + 71 + 142 = 220
*/

#include <stdio.h>
void main()
{
    int a,b;
    printf("Enter 2 numbers :");
    scanf("%d%d",&a,&b);
    int i,c=0,d=0;
    for(i=1;i<a;i++){
        if (a%i==0){
            c+=i;}
    }
     for(i=1;i<b;i++){
        if (b%i==0){
            d+=i;}
    }
    if (a==d && b==c)
        printf("%d & %d are amicable numbers",a,b);
    else 
        printf ("%d & %d are not amicable numbers",a,b);
   
}