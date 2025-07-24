#include <iostream.h>

void main()
{int a,i,min,max;
for(i=0;i<4;){
printf("Enter %dth element :",++i);
scanf("%d",&a);
if (i==1){
max=min=a;}
else {
if (a>max)
max=a;
if(a<min)
min=a;}}
printf ("minimum value is : %d \nmaximum value is : %d", min, max);

}