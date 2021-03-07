#include <bits/stdc++.h>
#include <bits/types/FILE.h>
#include <cmath>
using namespace std;
long long n;
bool isPrime()
{
  if(n < 2)
  {
    return false;
  }
  int mid = sqrt(n);
  for (int i = 2; i <= mid; i++) {
    if(n % i == 0)
      return false;
  }
  return true;
}
int main(int argc, char const* argv[])
{
  cin >> n;
  if (isPrime()) {
    cout << "YES";
  }
  else {
    cout << "NO";
  }
  return 0;
}

