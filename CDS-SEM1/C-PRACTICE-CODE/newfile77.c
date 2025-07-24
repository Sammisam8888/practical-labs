#include <iostream.h>
class M
{public :
void main (int i){
    cout<<"main with integer :"<<i<<endl;}
void main (double f){
    cout<<"main with double size float :"<<f<<endl;}
void main(char *s){
    cout<<"main with string :"<<s<<endl;}};
    
void main()
{M m;
m. main(8); //over loading case 1
m. main(6.894); //over loading case 2
m. main("Sammisam"); //overloading case 3
m. main (7.0); //overloading case 2
}