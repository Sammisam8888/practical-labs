#include <iostream.h>
class M{
    public :
    void h(){
        cout<<"Hihi";}};
class N : public M {
    public :
    void j(){
        h();        
        cout<<"jay";}};
class O : public N{
    public :
    void k(){
        j();  h();}};              
void main()
{O g;
g.k();
}