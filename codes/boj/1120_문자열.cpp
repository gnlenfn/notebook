#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    string a;
    string b;
    vector<int> answer;
    cin >> a >> b;
    int l = b.size() - a.size() + 1;
    for (int i = 0; i < l; i++)
    {
        int cnt = 0;
        for(int j = 0; j < a.size(); j++)
        {
            if(a[j] != b[j+i])
                cnt += 1;
        }
        answer.push_back(cnt);
    }
    cout << *min_element(answer.begin(), answer.end()) << endl;
}