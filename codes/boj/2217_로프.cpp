#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main()
{
    int n;
    cin >> n;
    vector<int> rope;
    for(int i = 0; i < n; i++)
    {
        int a;
        cin >> a;
        rope.push_back(a);
    }

    sort(rope.begin(), rope.end());
    
    vector<int> answer(n);
    for(int i = 0; i < rope.size(); i++)
        answer[i] = rope[i] * (n - i);
    
    int largest = answer[0];
    for(int i = 0; i < answer.size(); i++)
        largest = max(largest, answer[i]);

    cout << largest;
}