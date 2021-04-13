#include <bits/stdc++.h>
using namespace std;
int T, n, m, flag;
char cmap[510][510];
int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};
int dfs(int a, int b) {
  int x, y;
  if (cmap[a][b] == 't') {
    return 1;
  }
  for (int i = 0; i < 4; i++) {
    x = a + dx[i];
    y = b + dy[i];
    if (cmap[x][y] != 'x' && x >= 0 && x < n && y >= 0 && y < m) {
      cmap[a][b] = 'x';
      flag = dfs(x, y);
      if (flag == 1) {
        return 1;
      }
    }
  }
  return 0;
}
int main(int argc, char const *argv[]) {
  int a, b;
  cin >> T;
  while (T--) {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        cin >> cmap[i][j];
        if (cmap[i][j] == 's') {
          a = i;
          b = j;
        }
      }
    }
    if (dfs(a, b)) {
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }
  }
  return 0;
}
