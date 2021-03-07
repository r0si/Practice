#include <bits/stdc++.h>
#include <cmath>
#include <math.h>
using namespace std;
long long a , b, m,ans=1;
int main(int argc, char const *argv[]) 
{ 
  cin >> a >> b >> m;
  for (int i = 0; i < b; i++) {
    ans = (ans * a) % m;
  }
  cout << ans << endl;
  return 0; 
}
