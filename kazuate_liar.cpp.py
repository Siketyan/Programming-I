from subprocess import Popen, PIPE, call

name = "kazuate_liar.o"
src = """

#include <iostream>
#include <random>

using namespace std;

int main()
{
    random_device rd;
    mt19937 mt(rd());
    uniform_int_distribution<int> randfive(0, 4);
    uniform_int_distribution<int> randint(1, 100);

    int count = 0;
    int num = randint(mt);

    while (1)
    {
        int i;
        cout << "数を当ててみて ";
        cin >> i;

        if (i < 1 || i > 100)
        {
            cout << "不正な入力です。" << endl;
            continue;
        }

        count++;
        bool liar = randfive(mt) == 0;

        if (i == num)
        {
            cout << "正解です。おめでとう。 (" << count << " 回目)" << endl;
            break;
        }
        else if ((liar && i > num) || i < num)
        {
            cout << "もっと大きいよ。" << endl;
        }
        else
        {
            cout << "もっと小さいよ。" << endl;
        }
    }

    return 0;
}

""";

proc = Popen(["g++", "-o", name, "-x", "c++", "-"], stdin = PIPE);
proc.communicate(src.encode());
call(["./" + name]);

