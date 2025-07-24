#include <iostream.h>
using namespace std;
class X
{int *arr;
public :
X()
{arr=new int[10];
if (arr==NULL)
throw "exception";
else throw "exception - else block";}
~X()
{delete []arr;}};
void main()
{try{
    X x1;}
 catch (const char *m)
 {cout<<m;}}