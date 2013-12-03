#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;
struct A{
    A(){ cout << "ctor A\n"; }
    A(const A&){ cout << "cpy A\n"; }
    A(A&&){ cout << "move A\n"; }
    A& operator= (A&&) { cout << "move_assign A\n"; return *this; }
    A& operator= (const A&) { cout << "cpy_assign A\n"; return *this; }

    int t;
};

A create(){ return A{}; }

void test_move(){

    cout << "<<<\n";
    auto v = create();
    A v1{ create() };
    cout << "<<<\n";

    A v2 = v;

    A v3{ v };


    cout << "<<<\n";
    auto v_ = std::move(create());
    cout << "<<<\n";
    v = v_;
    cout << "<<<\n";
    v_ = std::move(v);
    cout << "<<<\n";

}

int main(int argc, char * argv []){
    test_move();

    return 0;
}