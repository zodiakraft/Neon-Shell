#include <iostream>
#include <cmath>
using namespace std;
int main() {
    int con;
    cin >> con;
    con %= 180;
    cout << "sin(" << con << ") = " << sin(con) << endl
         << "cos(" << con << ") = " << cos(con) << endl
         << "tg(" << con << ") = " << tan(con) << endl;
    return 0;
}