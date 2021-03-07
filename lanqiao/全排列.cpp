#include <algorithm>
#include <bits/stdc++.h>
#include <iostream>
#include <string>
using namespace std;
string s;
int main(int argc, char const *argv[]) {
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    s.append(to_string(i));
  }
  for (int i = 0; i < n; i++) {
    cout << s[i];
    if(i != n - 1)
    {
      cout << " ";
    }

  }
  cout << endl;
  while (next_permutation(s.begin(), s.end())) {
      for (int i = 0; i < n; i++) {
        cout << s[i];
        if(i != n - 1)
        {
          cout << " ";
        }
      }
      cout << endl;
    }
  return 0;
}
