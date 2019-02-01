from subprocess import Popen, PIPE, call

src = """

#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int n;
    cout << "学生の人数は? ";
    cin >> n;

    int student[n];
    for (int i = 0; i < n; i++)
    {
        cout << i + 1  << " 人目の点数は? ";
        cin >> student[i];
    }

    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        int score = student[i];
        sum += score;
        cout << i + 1 << " 人目の点数は " << score << " 点" << endl;
    }

    cout << "平均点は ";
    cout << setw(5) << right << fixed << setprecision(1) << (float) sum / n;
    cout << " 点です" << endl;
}

""";

proc = Popen(["g++", "-o", "heikin.o", "-x", "c++", "-"], stdin = PIPE);
proc.communicate(src.encode());
call(["./heikin.o"]);

