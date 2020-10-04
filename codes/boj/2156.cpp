#include <iostream>
#include <algorithm>
using namespace std;

int glass[10001], accum[10001], n;

void solution()
{
    accum[1] = glass[1];
    accum[2] = glass[1] + glass[2];
    for(int i = 3; i <= n; i++)
    {
        accum[i] = accum[i-1];                                            // i번 째 잔을 안마신 경우
        accum[i] = max(accum[i], accum[i-2] + glass[i]);                 // i번 째 잔이 연속 1잔인 경우 --> glass[i-1] x
        accum[i] = max(accum[i], accum[i-3] + glass[i-1] + glass[i]);   // i번 재 잔이 연속 2잔인 경우 --> glass[i-2] x
    }
    cout << accum[n] << endl;
}
int main()
{
    cin >> n;
    for(int i = 1; i <= n; i++)
        cin >> glass[i];
    solution();

    return 0;
}