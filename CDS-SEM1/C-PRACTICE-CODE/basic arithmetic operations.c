#include <stdio.h>
int add(int p, int q) 
{
    return p + q;
}
int sub(int p, int q) 
{
    return p - q;
}
int mul(int p, int q) 
{
    return p * q;
}
float div(int p, int q) 
{
    if (q == 0) 
	{
        return 0.0; 
    } 
	else 
	{
        return (float)p / q;
    }
}
int mod(int p, int q) 
{
        return p % q;
    }

int main() 
{
int p, q;
printf("enter two numbers:\n");
scanf("%d%d", &p, &q);
printf("addition of %d + %d = %d\n", p, q, add(p, q));
printf("subtraction of %d - %d = %d\n", p, q, sub(p, q));
printf("multiplication of %d * %d = %d\n", p, q, mul(p, q));
if (q!=0)
printf("division of %d / %d = %f\n", p, q, div(p, q));
else 
printf("division of %d & %d is not possible as denominator is 0\n",p,q);
printf("modulo of %d %% %d = %d\n", p, q, mod(p, q));
return 0;
}