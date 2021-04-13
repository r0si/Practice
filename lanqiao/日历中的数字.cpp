#include <bits/stdc++.h>
#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;
string y,m,x;
int cnt;
int leap(int year)
{
  if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
    return 1;
  }
  return 0;
}
int month(int m)
{
  switch (m) {
    case 1:
      return 31;
      break;
    case 2:
      if (leap(stoi(y)) == 1) {
        return 29;
      }
      return 28;
    case 3:
      return 31;
    case 4:
      return 30;
    case 5:
      return 31;
    case 6:
      return 30;
    case 7:
      return 31;
    case 8:
      return 31;
    case 9:
      return 30;
    case 10:
      return 31;
    case 11:
      return 30;
    case 12:
      return 31;
  }
  return 0;
}
int main(int argc, char const* argv[])
{
  while (cin >> y >> m >> x) {
    cnt = 0;
    if (m.length() < 2) {
      m.insert(0,"0");
    }
    //string str = y + m;
    //cout << str <<endl;
    string day;
    for (int i = 1; i <= month(stoi(m)); i++) {
      if (i < 10) {
        day = "0" + to_string(i);
      }
      else {
        day = to_string(i);
      }
      string str = y + m + day;
      //cout << str << endl;
      for (int j = 0; j < str.length(); j++) {
        if (str[j] == x[0]) {
          cnt++;
        }
      }
    }
    cout << cnt <<endl;
  }
  return 0;
}
