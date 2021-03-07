#include <bits/stdc++.h>
#include <cmath>
#include <cstdio>
#include <fenv.h>
#include <ostream>
using namespace std;
int m;
/*
bool isPrime(int a) {
  if (a <= 3) {
    return a > 1;
  }
  int _sqrt = sqrt(a);
  for (int i = 4; i <= _sqrt; i++) {
    if (a % i == 0)
      return false;
  }
  return true;
}
*/
/*
int gcd(int a, int b) {
  if (b == 0) {
    return a;
  }
  return gcd(b, a % b);
}
*/
/*
int gcd(int a,int b)
{
  int t = 1;
  while (t!=0) {
    t = a%b;
    a=b;
    b=t;
  }
  return a;
}*/
int euler_phi(int n){
  int ans = n;
  for (int i = 2; i*i <= n; i++) {
    if (n%i==0) {
      ans = ans / i * (i - 1);
      while (n % i ==0) {
        n /= i;
      }
    }  
  }
  if (n > 1)
    ans = ans / n * (n - 1);
  return ans;
}
int main(int argc, char const* argv[])
{
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int q;
    cin >> q;
    cout << euler_phi(q) << endl;
  }
  return 0;
}
/*
int main(int argc, char const *argv[]) {
  cin >> m;
  for (int i = 0; i < m; i++) {
    int n, cnt = 0;
    cin >> n;
    for (int i = 1; i <= n; i++) {
      if (gcd(i, n) == 1) {
        cnt++;
      }
    }
    cout << cnt << endl;
  }
  return 0;
}
*/
