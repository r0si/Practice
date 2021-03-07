#include <bits/stdc++.h>
using namespace std;
long long a, b, m;
long long mul_mod(long long a, long long b, long long m) {
  long long res = 0;
  while (b) {
    if (b & 1) {
      res = (res + a) % m;
    }
    a = (a + a) % m;
    b >>= 1;
  }
  return res;
}
int main(int argc, char const *argv[]) {
  cin >> a >> b >> m;
  cout << mul_mod(a, b, m) << endl;
  return 0;
}
