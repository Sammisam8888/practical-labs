/*
2. Define a class car rental with following details :
i - car_id - int 
    car_type - string
    rent - float
    
Define a getchar() method to accept carid, cartype and return the rent of the car - for car type :
small car - 1000, van - 800, suv - 2500
Show_car()- method which allows users to view the contents of cars ie id,type and rent
*/


#include <iostream>
using namespace std;

class CarRental{
    int carid;
    string car_type;
    float rent;
    public:
    void getdata();
    float getrent();
    void showcar();
};
void CarRental::getdata(){
    cout<<"Enter the details of the car : "<<endl;
    cout<<"Enter the car ID : ";
    cin>>carid; 
    cout<<"Enter the car type (small car/van/suv) : ";
    cin.ignore();
    getline(cin,car_type);
    rent=getrent();
}
float CarRental::getrent(){
    if (car_type=="small car") return 1000;
    else if (car_type=="van") return 800;
    else if (car_type=="suv") return 2500;
    return 0;
}
void CarRental::showcar(){
    cout<<"The car ID is : "<<carid<<endl;
    cout<<"The car type is : "<<car_type<<endl;
    cout<<"The Rent is : "<<rent<<endl;
}

int main(){
    CarRental C;
    C.getdata();
    C.showcar();
    return 0;
}
