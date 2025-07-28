#include <stdio.h>
#include<conio.h>
float area(float radius) {
    //float pie = 3.14;
  return pie * radius * radius;
}
float circum(float radius) {
    //float pie = 3.14;
  return 2 *pie * radius;
}

void main() {
 const int pie=3.14;
 float radius;
 printf("Enter radius: ");
 scanf("%f", &radius);
 printf("Area : %.3f\n", area(radius));
 printf("Circumference: %.3f\n", circum(radius));
}

getch();}