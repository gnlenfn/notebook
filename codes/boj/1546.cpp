#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    int n, p;
    cin >> n;

    for(int i = 0; i < n; i++)
    {
        cin >> p;
        vector<pair<int, string>> member(p);
        int maxVal = 0, idx;
        for(int i = 0; i < p; i++)
        {
            cin >> member[i].first >> member[i].second;
            if (member[i].first > maxVal)
            {
                maxVal = member[i].first;
                idx = i;
            }
        }
       cout << member[idx].second << endl;
    }
}