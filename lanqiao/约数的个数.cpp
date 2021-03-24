#include <bits/stdc++.h>
using namespace std;
int n,cnt=0;
int main(int argc, char const* argv[])
{
  cin >> n;
  for (int i = 1; i <= n / 2; i++) {
    if (n % i == 0) {
      cnt++;
    }
  }
  cout << cnt << endl;
  return 0;
}
