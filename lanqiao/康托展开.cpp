#include <algorithm>
#include <bits/stdc++.h>
using namespace std;
string s,s1="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
int n;
int main(int argc, char const* argv[])
{
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> s;
    int num = 1;
    /*
    for (int j = 0; j < s.size(); j++) {
      s1[i] = 'A';
    }
    */
    s1 = s1.substr(0,s.size());
    cout << s1 << s.size() << " " << endl;
    if (s == s1) {
      cout << num << endl;
      continue;
    }
    while (next_permutation(s.begin(),s.end())) {
      num++;
      if (s == s1) {
        cout << num << endl;
        break;
      }
    }
  }
  return 0;
}
