#include <bits/stdc++.h>
using namespace std;
long gcd(long a,long b){
  if (a % b ==0) {
    return b;
  }
  return gcd(b,a%b);
}
long lcm(long a,long b){
  return a*b/gcd(a,b);
}
int main(int argc, char const* argv[])
{
  long a,b;
  cin >> a>>b;
  cout << lcm(a,b);
  return 0;
}
