#include <stdio.h>
int main() {
  int a[]={11,22,33,44,55};
  int del;
  printf("enter the position from where element to be deleted...");
scanf("%d", &del);
  for(int i=0; i<5; i++)
  {
    if(i==del){
for (int j=i;j<4;j++){
if (j<=4)
a[j]=a[j+1];}
a[4]=0;}
 printf("%d, ",a[i]);   }
    return 0;
}