#include <bits/stdc++.h>
#include <queue>
using namespace std;
queue<int> quem,quen;
int m,n,k;
int main(int argc, char const* argv[])
{
  cin >> m >> n >> k;
  for (int i = 1; i <= m; i++) {
    quem.push(i);
  }
  for (int i = 1; i <= n; i++) {
    quen.push(i);
  }
  for (int i = 1; i <= k; i++) {
    int tempm,tempn;
    cout << quem.front() << " " << quen.front() << endl;
    //tempm = quem.front();
    //tempn = quen.front();
    quem.push(quem.front());
    quem.pop();
    quen.push(quen.front());
    quen.pop();
  }
  return 0;
}
