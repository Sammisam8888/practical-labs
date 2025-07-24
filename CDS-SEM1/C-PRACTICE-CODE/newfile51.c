#include <iostream.h>
#include <conio.h>
class jio{
    int mukesh,anil;
    public :
    void in(){
        cout<<"Enter 2 numbers :";
        cin>>mukesh>>anil;}
     void operator--(){
         mukesh--;
         anil--;}
     void operator++(){
         mukesh++;
         anil++;}
      void operator-(){
          mukesh=-mukesh;
          anil=-anil;}
 void display(){
cout<<mukesh<<" "<<anil<<"\n";}};
void main()
{clrscr();
jio ambani;
ambani.in();
--ambani;
ambani.display();
-ambani;
ambani.display();
++ambani;
ambani.display();
getch();}