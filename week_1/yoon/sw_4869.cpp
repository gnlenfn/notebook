#include <iostream>
using namespace std;

int arr[31] {0};
int dp(int n)
{
    int x = n / 10;
    arr[1] = 1;
    arr[2] = 3;

    for(int i = 3; i < 31; ++i)
    {
        arr[i] = arr[i-1] + 2 * arr[i-2];
    }
    return arr[x];
    
}

int main()
{
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i)
    {
        int n;
        cin >> n;
        cout << "#" << i << " " << dp(n) << endl;
    }
}