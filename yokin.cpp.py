from subprocess import Popen, PIPE, call

name = "yokin.o"
src = """

#include <iostream>
using namespace std;

int main()
{
    int balance = 10000;
    int years = 0;

    while (balance <= 15000)
    {
        balance *= 1.05;
        years++;
    }

    cout << "The balance will be greater than 15000 JPY after " << years << " years." << endl;
    return 0;
}

""";

proc = Popen(["g++", "-o", name, "-x", "c++", "-"], stdin = PIPE);
proc.communicate(src.encode());
call(["./" + name]);

