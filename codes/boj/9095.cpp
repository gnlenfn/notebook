#include <iostream>
using namespace std;

int sp[11] = {0,1,2,4};
int solution(int x)
{
    
    for(int i = 4; i <= x; i++)
    {
        sp[i] = sp[i-1] + sp[i-2] + sp[i-3];
    }
    return sp[x];
}

int main()
{
    int t;
    cin >> t;
    for(int i = 0; i < t; ++i)
    {
        int n;
        cin >> n;
        cout << solution(n) << endl;
    }
    return 0;
}

