//wap to print the 3 smallest digits in a mobile number

#include <stdio.h>
void smallsort(long int n){
    int a[10],i=0,t,j;
    while (n>0){ //long int to array by individual element
        a[i]=n%10;
        n/=10;
        i++;
    }
    for(i=0;i<10;i++){ //sort in array 
        for (j=0;j<i;j++){
             if (a[i]<a[j]){
                 t=a[i];a[i]=a[j];a[j]=t;
         }
        }
    }
    printf("The three smallest digits are : %d%d%d",a[0],a[1],a[2]);
}
     
int main()
{
    long int d;
    printf("Enter your mobile number :");
    scanf("%ld",&d);
    smallsort(d);
    return 0;
}