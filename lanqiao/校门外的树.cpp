#include <bits/stdc++.h>
#include <cmath>
#include <cstring>
using namespace std;
int L,M,cnt;
int ans[10010];
int main(int argc, char const* argv[])
{ 
  while (cin >> L >> M) {
    int a,b;
    cnt = 0;
    memset(ans,1,sizeof(ans));
    for (int i = 0; i < M; i++) {
      cin >> a >> b;
      for (int i = a; i <= b; i++) {
        ans[i] = 0;
      }
    }
    for (int i = 0; i <= L; i++) {
      if (ans[i]) {
        cnt++;
      }
    }
    cout << cnt << endl;
  }
  return 0;
}
