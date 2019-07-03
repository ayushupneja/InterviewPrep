#include <bits/stdc++.h>

using namespace std;

// Complete the countingValleys function below.
int countingValleys(int n, string s) {
    int runsum = 0;
    int counter = 0;
    int checker = 0;
    // checker 0 means not activated, 1 is activated
for (int i=0; i<n;i++) {
    cout << runsum << endl;
    if (runsum == 0 && i!=0)
        checker = 1;
    if (s.at(i) == 'U') {
        runsum+=1;
        if (checker == 1) {
        checker = 0;
        }
    }
    if (s.at(i) == 'D') {
        runsum-=1;
        if (checker == 1){
            counter+=1;
            checker = 0;
        }
    }
    if (i == 0){
        if (runsum < 0) {
            counter+=1;
        }
    }

}
return counter;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string s;
    getline(cin, s);

    int result = countingValleys(n, s);

    fout << result << "\n";

    fout.close();

    return 0;
}
