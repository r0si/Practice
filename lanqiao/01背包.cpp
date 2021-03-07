#include <algorithm>
#include <bits/stdc++.h>
using namespace std;
const int maxn = 1010;
int dp[maxn], v[maxn], w[maxn];
int main(int argc, char const *argv[]) {
  int n, W;
  cin >> n >> W;
  for (int i = 1; i <= n; i++) {
    cin >> w[i] >> v[i];
  }
  for (int i = 1; i <= n; i++) {
    for (int j = W; j >= w[i]; j--) {
      dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
    }
  }
  cout << dp[W];
  return 0;
}
