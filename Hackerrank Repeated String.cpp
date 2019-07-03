#include <bits/stdc++.h>

using namespace std;

// Complete the repeatedString function below.
long repeatedString(string s, long n) {
    int acounter = 0;
    int remainder = 0;
    int remainderCount = 0;
    long long int answer;
    remainder = n%s.size();
    for (int i = 0;i<s.size();i++){
        if (s.at(i) == 'a'){
            acounter+=1;
        }
        if (i+1 == remainder && remainder!=0) {
            remainderCount = acounter;
        }
    }
    long long int multiplier = n/s.size();
    answer = multiplier * acounter + remainderCount;
    return answer;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    long n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    long result = repeatedString(s, n);

    fout << result << "\n";

    fout.close();

    return 0;
}
