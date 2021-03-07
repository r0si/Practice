#include <bits/stdc++.h>
using namespace std;
int a[30]={0,1,2,4},n;
int main(int argc, char const* argv[])
{
  cin >> n;
  for (int i = 4; i <= n; i++) {
    a[i] = a[i-1] + a[i-2] + a[i-3];
  }
  cout << a[n] << endl;
  return 0;
}
