#include <bits/stdc++.h>
using namespace std;
int main(int argc, char const* argv[])
{
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int year;
    cin >> year;
    if ((year%4==0&&year%100!=0)||year%400==0) {
      cout << "Yes"  << endl;
    }
    else{
      cout << "No" << endl;
    }
  }
  return 0;
}
