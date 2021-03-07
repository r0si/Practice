#include <bits/stdc++.h>
using namespace std;
long long a, b, m, ans = 1;
long long binpow()
{
  a %= m;
  long long res = 1;
  while (b > 0) {
    if (b & 1) {
      res = res * a % m;
    }
    a = a * a % m;
    b >>= 1;
  }
  return res;
}
int main(int argc, char const *argv[]) {
  cin >> a >> b >> m;
  
  cout << binpow() << endl;
  return 0;
}
