#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e5 + 10;
int fac[maxn];
long n, t = 2, i = 0;
int main(int argc, char const *argv[]) {
  cin >> n;
  while (n != 1) {
    if (n % t == 0) {
      n /= t;
      if (i != 0 && fac[i - 1] == t) {
        fac[i - 1] = t;
      } else {
        fac[i++] = t;
      }
    } else {
      t++;
    }
  }
  for (int i = 0; i < t; i++) {
    if (fac[i] == 0) {
      break;
    }
    cout << fac[i] << " ";
  }
  return 0;
}
