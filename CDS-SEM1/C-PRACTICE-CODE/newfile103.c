//Write a program to input a time in second's and convert it into Hours, Minute and Seconds and print the results in following format. (E.g. If the given time is 12035 seconds, then it will be printed as 3H: 20M: 35S)

#include <stdio.h>
void time(long int n){
    int d, h,m,s;
    m=n/60;
    h=m/60;
    s=n%60;
    m=m%60;
    d=h/60;
    h=h%60;
    printf("Time : %02d days:%02d hours:%02d mins:%02d sec",d,h,m,s);  
}
void main()
{
        long int n;
        printf("Enter a time(in seconds) :");
        scanf("%ld",&n);
        time(n);

}