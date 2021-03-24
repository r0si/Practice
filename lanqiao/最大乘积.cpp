#include <bits/stdc++.h>
using namespace std;
int n;
int a[20];
int main(int argc, char const* argv[])
{
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  double max_result = a[0];
  for (int i = 0; i < n; i++) {
    double ans = 1;
    for (int j = i; j < n; j++) {
      ans *= a[j];
      if (ans > max_result) {
        max_result = ans;
      }
    }
  }
  if (max_result < 0) {
    cout << "0" << endl;
  }
  cout << max_result << endl;
  return 0;
}
