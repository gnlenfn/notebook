#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int array[n+1];

    for(int i = 0; i < n; i++)
        cin >> array[i];

    int answer[n+1];
    for(int i = 0; i < n; i++)
        answer[i] = 1;
    
    for(int i = 0; i < n; i++)
    {
        for(int j = i-1; j >= 0; j--)
        {
            if(array[j] < array[i] && answer[j] >= answer[i])
                answer[i] = answer[j] + 1;
        }
    }

    int max= -1;
    for(int i = 0; i < n; i++)
        if(max < answer[i]) max = answer[i];
    
    cout << max << endl;

}