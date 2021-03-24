#include <bits/stdc++.h>
using namespace std;
int n,k,mod=0;
int main(int argc, char const* argv[])
{
  cin >> n >> k;
  for (int i = 1; i <= n; i++) {
    mod = mod + k % i;
  }
  cout << mod << endl;
  return 0;
}
