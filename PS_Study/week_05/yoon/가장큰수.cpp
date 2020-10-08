#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool compare(string a, string b)
{
    return a + b > b + a;                                   // string 으로 전환된 숫자를 더해서 큰 것 return
}                                                           // [10, 9]에서  109와 910 비교
string solution(vector<int> numbers) {
    string answer = "";
    vector<string> tmp;
    for(auto n : numbers)
        tmp.push_back(to_string(n));
    
    sort(tmp.begin(), tmp.end(), compare);                  // compare 함수에 따라 정렬
    if(tmp.at(0) == "0") return "0";                        // 첫 문자가 0이면 전체가 0이므로 0 return
    
    for(auto t : tmp)                                       // 정렬된 벡터의 요소를 모두 이어서 출력
        answer += t;

    return answer;
}

int main()
{
    vector<int> numbers={6, 10, 2};
    vector<int> num2 = {3, 30, 34, 5, 9};
    std::cout << solution(numbers) << std::endl;
    //std::cout << solution(num2) << std::endl;
}