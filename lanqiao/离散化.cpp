#include <bits/stdc++.h>
#include <cmath>
#include <cwctype>
#include <ratio>
using namespace std;
const int maxn = 1e5+10;
long n,a[maxn],tmp[maxn];
int main(int argc, char const* argv[])
{
  int step = 1,t;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> a[i];
    tmp[i] = a[i];
  }
  sort(a+1,a+n+1);
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      if (a[i]==tmp[j]) {
        if (t==a[j]) {
          cout << step << " ";
          break;
        }
        else {
          cout << j << " ";
          t = a[i];
          step = j;
          //step++;
          break;
        }
      }
    }
  }
  return 0;
}
