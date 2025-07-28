//wap to return pointer type in function

#include <stdio.h>
int* fun(int i){
    return &i;}
void main()
{
int x=5;
int *p=fun(x);
printf("%d",*p);
}