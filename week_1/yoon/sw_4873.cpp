#include <iostream>
#include <stack>
#include <string>
using namespace std;

int solution(string line)
{
    stack<char> s;

    for(int i = 0; i < line.size(); ++i)
    {
        if(s.size() == 0) s.push(line[i]);
        else
        {
            if(s.top() == line[i]) s.pop();
            else s.push(line[i]);
        }
        
    }
    int length = s.size();

    return length;
}

int main()
{
    int t, result;
    cin >> t;
    string line;
    getline(cin, line);

    for(int i = 1; i <= t; ++i)
    {
        getline(cin ,line);
        result = solution(line);

        cout << "#" << i << " " << result << endl;
    }
    return 0;
}