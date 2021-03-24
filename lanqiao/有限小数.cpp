#include <iostream>
using namespace std;

int gcd(int x, int y) {
  if (x % y == 0) {
    return y;
  }
  return gcd(y, x % y);
}

bool is2And5Number(int n) {
  while (0 == n % 2) {
    n /= 2;
  }

  while (0 == n % 5) {
    n /= 5;
  }

  if (1 == n) {
    return true;
  }

  return false;
}

int main() {
  int a, b;
  int g, n;
  char c;
  cin >> a >> c >> b;
  g = gcd(a, b);
  n = b / g;

  if (is2And5Number(n)) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }

  return 0;
}
