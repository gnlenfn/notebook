#include <iostream>
using namespace std;

int main()
{
    int paper, result = 0;
    cin >> paper;
    int n = 1000 - paper;

    result += n / 500;
    n %= 500;
    
    result += n / 100;
    n %= 100;
    
    result += n / 50;
    n %= 50;
    
    result += n / 10;
    n %= 10;
    
    result += n / 5;
    n %= 5;
    
    result += n / 1;

    cout << result << endl;
    return 0;
}