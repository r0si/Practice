#include <algorithm>
#include <bits/stdc++.h>
#include <cstdio>
using namespace std;
int n,m,a[10100];
int main(int argc, char const* argv[])
{
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    cout << a[i] << " ";
  }
  m--;
  cout << endl;
  while (prev_permutation(a,a+n)!=0 && m--) {
    for (int i = 0; i < n; i++) {
      cout << a[i] << " ";
    }
    cout << endl;
  }
  return 0;
}
