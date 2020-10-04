#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    long long x, y;
    int w, s;
    cin >> x >> y >> w >> s;
    long long mod = (x + y) % 2;
    if(x < y) swap(x, y);
    cout << min((x + y) * w, min((x - mod) * s + mod * w, y * s + (x-y) * w)) << endl;
}

// 1. 한 블럭씩 이동
// 2. 대각선으로 이동 후 남은 만큼 블럭 이동
// 3. 