//Q - 

#include <stdio.h>

int* fun(){
    int x=5;
    int *p=&x;
    return p;
}
void main()
{
    
    int *x=fun();
    
    printf("%d",*x);
}