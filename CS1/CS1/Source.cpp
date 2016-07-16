#include <stdlib.h>
#include <iostream>
using std::cout;
using std::cin;
using std::endl;
using std::fixed; //ensures that decimal point is displayed

#include <iomanip>
using std::setprecision; //sets numeric output precision


int addtwo(int a, int b) {
   return a*b;
}

int main() {
   int a = 5;
   int b = 6;
   int c = addtwo(a, b);
   cout << c;
}

