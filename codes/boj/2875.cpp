#include <iostream>
using namespace std;

int main()
{
    int n, m, k;
    cin >> n >> m >> k;
    int team = 0, total = n + m - k;

    while(n >= 2 && m >= 1 && total >= 3)
    {
        n -= 2;
        m -= 1;
        total -= 3;

        team += 1;
    }
    cout << team << endl;    

    return 0;
}