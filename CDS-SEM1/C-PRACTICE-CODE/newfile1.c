#include <stdio.h>
void main()
{
	int a =8;
	int b = a++ + a--; 
	// left to right normal due to equation
    printf ("%d \n%d",a,b);
    
}