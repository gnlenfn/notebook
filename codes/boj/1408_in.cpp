#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;


template<typename Out>
void split(const string &s, char delim, Out result)
{
    stringstream ss(s);
    string item;

    while (getline(ss, item, delim))
        *(result++) = item;
}

vector<string> split(const string &s, const char delim)
{
    vector<string> elems;
    split(s, delim, back_inserter(elems));
    return elems;
}

//void printResult()
int main()
{
    string now;
    string start;

    cin >> now >> start;

    vector<string> TimeNow = split(now, ':');
    vector<string> TimeStart = split(start, ':');

    int sec = stoi(TimeStart[2]) - stoi(TimeNow[2]);
    int min = stoi(TimeStart[2]) - stoi(TimeNow[1]);
    int hour = stoi(TimeStart[0]) - stoi(TimeNow[0]);

    if (sec < 0) 
    {
        sec = 60 - sec;
        if (min < 0)
        {
            min = 60 - min - 1;
            hour = hour - 1;
        } 
        else min = min - 1;
    }
    else
    {
        if(min < 0) 
        {
            min = 60 - min;
            hour = hour - 1;
        }

    }

    

}