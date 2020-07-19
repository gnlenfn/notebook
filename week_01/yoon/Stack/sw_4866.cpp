#include <iostream>
#include <string>
#include <stack>
using namespace std;

int solution(string line)
{
    stack<char> s;
    for(int j = 0; j < line.size(); ++j)
    {
        if(line[j] == '(' | line[j] == '{')
            s.push(line[j]);
        
        else if(line[j] == ')' | line[j] == '}')
        {
            if(s.size() == 0)
            {
                s.push(line[j]);
                break;
            }
            else if((line[j] == ')' && s.top() != '(') | (line[j] == '}' && s.top() != '{'))
            {
                s.push(line[j]);
                break;
            }
            else
            {
                s.pop();
            }
        }   
    }
    if(s.size() == 0)
        return 1;
    else
        return 0;
    
}


int main()
{
    int t;
    cin >> t;
    int result;
    std::string line;
    std::getline(cin, line);
    for(int i = 1; i <= t; ++i)
    {        
        std::getline(cin, line);
        result = solution(line);

        cout << "#" << i << " " << result << endl;

    }

    //cout << result;
} 