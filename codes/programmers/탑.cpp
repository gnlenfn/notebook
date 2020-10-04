#include <string>
#include <vector>
#include <stack>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> heights) {
    vector<int> answer;
    stack<int> st;
    bool check = true;
    for(int i = heights.size()-1; i >= 0; i--)
    {
        for(int j = i - 1; j >= 0; j--)
        {
            if(heights.at(i) < heights.at(j))
            {
                st.push(j+1);
                check = false;
                break;
            }
        }
        if(check)
            st.push(0);
        check = true;
    }
    while(!st.empty())
    {
        answer.push_back(st.top());
        st.pop();
    }
    
    return answer;
}

void print(vector<int> heights)
{
    vector<int> t = solution(heights);
    for(auto &e : t)
        cout << e << " ";
    cout << endl;

}

int main()
{
    print({6,9,5,7,4});
    print({3,9,9,3,5,7,2});
    print({1,5,3,6,7,6,5});
}