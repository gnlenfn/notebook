#include <iostream>
#include <vector>
#include <string>
using namespace std;

typedef struct student
{
    string name;
    int day;
    int month;
    int year;
};

int main()
{
    int n;
    cin >> n;

    student *k = new student [n];
    for(int i = 0; i < n; i++)
        cin >> k[i].name >> k[i].day >> k[i].month >> k[i].year;

    student Young = k[0], Old = k[0];
    for(int i = 1; i < n; i++)
    {
        if (k[i].year > Young.year) Young = k[i];
        else if (k[i].year < Old.year) Old = k[i];
        else if (k[i].year == Young.year)
        {
            if (k[i].month > Young.month) Young = k[i];
            else if (k[i].month == Young.month)
                if (k[i].day > Young.day) Young = k[i];
        }
        else if (k[i].year == Old.year)
        {
            if (k[i].month < Old.month) Old = k[i];
            else if (k[i].month == Old.month)
                if (k[i].day < Old.day) Old = k[i];
        }
    }
    std::cout << Young.name << endl;
    std::cout << Old.name << endl;
}