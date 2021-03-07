#include <bits/stdc++.h>
using namespace std;
long a[50] = {0,1,1,3};
int main(int argc, char const* argv[])
{
  long k,n;
  cin >> k;
  for (int i = 4; i <= k; i++) {
    a[i] = (a[i-1]+a[i-2])*2;
  }
  cout << a[k] << endl;
  return 0;
}
