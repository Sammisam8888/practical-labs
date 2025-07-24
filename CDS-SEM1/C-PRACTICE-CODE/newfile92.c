//Q13
#include <stdio.h>
int factorial(int n){
    int i,f=1;
    if (n==0)
    f=0;
    else{
    for(i=1;i<=n;i++){
        f*=i;}}
    return f;}  
void main(){
int n,i; float s=0;
printf ("Enter a number n : ");
scanf("%d",&n);
for (i=1;i<=n;i++){
    s+=(float)(1/factorial(i));}    
printf("The sum of the pattern for n nos is : %f",s);   
}