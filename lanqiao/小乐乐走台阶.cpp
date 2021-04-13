#include <bits/stdc++.h>
using namespace std;
int n,ans[50]={0,1,2};
int main(int argc, char const* argv[])
{
  while (cin >> n) {
    for (int i = 3; i <= n; i++) {
      ans[i] = ans[i-1] + ans[i-2];
    }
    cout << ans[n] << endl;
  }
  return 0;
}
