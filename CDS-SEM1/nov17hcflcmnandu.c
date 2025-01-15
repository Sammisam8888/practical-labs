#include<stdio.h>
int factor(int a,int b)
{ int i,j,h,max=0,g;
 
 if(a<b){
 
 for(i=1;i<=a;i++)
 { if(a%i==0 && b%i==0)
    { if(max<i)
      { max=i;
	  }
	}
 } 
 printf("The HCF of the number is %d",max);}
if(a>b){
 
 for(i=1;i<=b;i++)
 { if(a%i==0 && b%i==0)
    { if(max<i)
      { max=i;
	  }
	}
 } 
 printf("The HCF of the number is %d",max);}
 
g=a*b;
 for(j=1;j<=a;j++)
  { int m=a*j;
     for(h=1;h<=b;h++)
       { int n=b*h;
        if(m==n)
        { if(g>m)
          { g=m;
		  }
		}
         
		   }
		 }
		 printf("\nThe LCM of the number is %d",g);
	    
	

  

 
 return max;
}
int main()
{ int x,y;
 printf("Enter any two number:\n");
 scanf("%d %d",&x,&y);
 factor(x,y); 
}