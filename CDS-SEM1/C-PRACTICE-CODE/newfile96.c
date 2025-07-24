#include <iostream.h>
void fun(int n){
    if (n<1) return;
    cout<<n;
    fun(n-1);
    cout<<n;
}
void main()
{
fun(3);
}