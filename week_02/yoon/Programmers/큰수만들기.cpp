#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string solution(string number, int k) {
    string answer = "";
    for(int i = 0, index = -1; i < number.length() - k; i++)        // number의 처음부터 끝까지 이동
    {
        char max = 0;
        for(int j = index + 1; j <= k + i; j++)                     // index에서 
        {
            if(max < number[j])
            {
                max = number[j];
                index = j;
            }
        }
        answer += max;
    }
    return answer;
}


int main()
{
    cout << solution("1924", 2) << endl;
    cout << solution("1231234", 3) << endl;
    cout << solution("4177252841", 4) << endl;

    return 0;
}
