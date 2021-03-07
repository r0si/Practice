#include <bits/stdc++.h>
#include <fstream>
using namespace std;
int n;
struct node {
  string name;
  int verbal;
  int math;
  int english;
  int sum;
} a[1010];
bool cmp(node x, node y) {
  if (x.sum != y.sum) {
    return x.sum > y.sum;
  } else if (x.verbal != y.verbal) {
    return x.verbal > y.verbal;
  } else if (x.math != y.math) {
    return x.math > y.math;
  } else
    return x.english >= y.english;
}
int main(int argc, char const *argv[]) {
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a[i].name >> a[i].verbal >> a[i].math >> a[i].english;
    a[i].sum = a[i].verbal + a[i].math + a[i].english;
  }
  sort(a, a + n, cmp);
  for (int i = 0; i < n; i++) {
    cout << a[i].name << " " << a[i].verbal << " " << a[i].math << " "
         << a[i].english << endl;
  }
  return 0;
}
