#include <graphics.h>

#include <stdio.h>

#include <stdlib.h>

#include <conio.h>

#include <dos.h>

void main(){

clrscr();

int graphdriver=0,graphmode:

initgraph(&graphdriver, &graphmode, "C:\TurboC++BGI");

while(!kbhit()){

setcolor(random(16));

circle(random(getmaxx()), random(getmaxy()), random(100)); delay(100);}

getch();}