#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    string word;
    cin >> word;
    vector<int> alpha(26);
    fill(alpha.begin(), alpha.end(), -1);
    for(int i = 0; i < word.size(); i++){
        int tmp = word[i];
        int a = 'a';
        if (alpha[tmp - a] == -1){
            alpha[tmp - a] = i;
        }
    }
    for(int i = 0; i < 26; i++)
        cout << alpha[i] << " ";
    cout << endl;
} 