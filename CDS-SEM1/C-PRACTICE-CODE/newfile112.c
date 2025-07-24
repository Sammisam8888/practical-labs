//Q - print the structure
/*
         1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5
*/

#include <stdio.h>
void main()
{
    for (int i=1;i<=5;i++){
        for(int z=5-i;z>0;z--){
        printf("   ");}
        for (int j=;j<=i;j++){
            printf("%d ",j);
        }
        for (int k=i+1;k>2;k--){
            printf("%d ",k);}
            printf("\n");
    }
    
}