#include <algorithm>
#include <bits/stdc++.h>
using namespace std;
int T, M;
int dp[1010], w[1010], v[1010];
int main(int argc, char const *argv[]) {
  cin >> T >> M;
  for (int i = 1; i <= M; i++) {
    cin >> w[i] >> v[i];
  }
  for (int i = 1; i <= M; i++) {
    for (int j = T; j >= w[i]; j--) {
      dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
    }
  }
  cout << dp[T] << endl;
  return 0;
}
