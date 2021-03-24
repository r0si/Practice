#include <bits/stdc++.h>
#define ll long long
using namespace std;
void exgcd(ll a, ll b, ll &x, ll &y) {
  if (!b)
    x = 1, y = 0;
  else {
    exgcd(b, a % b, y, x);
    y -= (a / b) * x;
  }
}
int main() {
  ll a, b, x, y;
  scanf("%lld%lld", &a, &b);
  exgcd(a, b, x, y);
  printf("%lld", (x + b) % b);
  return 0;
}
