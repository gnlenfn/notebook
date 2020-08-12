#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    sort(citations.begin(), citations.end(), greater<int>());
    // for(auto &e : citations)
    //     cout << e << " ";
    // cout << endl;
    for(int i = 0; i < citations.size(); i++)
    {
        if(citations[i] > i) ++answer;
        else break;
    }
    return answer;
}

int main()
{
    vector<int> arr = {0, 1, 3, 5, 5, 5, 5, 5, 5, 6};
    cout << solution(arr) << endl;
}