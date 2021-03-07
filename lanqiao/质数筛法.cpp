#include <bits/stdc++.h>
#include <cstring>
using namespace std;
const int maxn = 1e5+10;
int m,a[maxn];
void prime()
{
  memset(a,1,sizeof(a));
  a[0]=a[1]=0;
  int t = sqrt(maxn);
  for (int i = 2; i <= t; i++) {
    for (int j = 2 * i; j <= maxn; j+=i) {
      a[j]=0;
    }
  }
  return;
}
int main(int argc, char const* argv[])
{
  cin >> m;
  prime();
  for (int i = 0; i < m; i++) {
    int x;
    cin >> x;
    if (a[x]) {
      cout << "YES" << endl;
    }
    else {
      cout << "NO" << endl;
    }
  }
  return 0;
}
