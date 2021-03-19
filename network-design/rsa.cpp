#include <bits/stdc++.h>
#include <cmath>
#include <math.h>

using namespace std;
// m = 2  p = 3 q = 17
#define ll long long

ll p, q, eular, e;
double d, m, N, c, c1;

int gcd(int a, int b) {
  if (a % b == 0) {
    return b;
  }
  return gcd(b, a % b);
}

int prime(int n) {
  if (n < 2) {
    return 0;
  }

  int mid = sqrt(n);
  for (int i = 2; i <= mid; i++) {

    if (n % i == 0) {

      return 0;
    }
  }

  return 1;
}

void rsa_encrypt() {

  cout << "Please input m:";

  cin >> m;

  cout << "Please input p:";

  cin >> p;

  cout << "Please input q:";

  cin >> q;

  if (prime(p) == 0 || prime(q) == 0) {

    cout << "p and q must be is prime!" << endl;

    return;
  }

  if (p == q) {

    cout << "p must not equal q!" << endl;

    return;
  }

  N = p * q;

  // cout << N << endl;

  eular = (p - 1) * (q - 1);

  // cout << eular << endl;

  // cout << "Please input e (e < eular)" << "eular: " << eular;

  // cout << "e:";

  // cin >> e;

  e = 2;

  while (e < eular) {

    if (gcd(eular, e) == 1) {

      break;

    } else {

      e++;
    }
  }

  // cout << e << endl;

  /*

  int k = 1;



  while ((eular * k + 1) % e != 0) {

    k++;

  }

  d = (eular * k + 1) / e;

  */

  d = 1 / (double)e;

  d = fmod(d, eular);

  c1 = pow(m, e);

  // cout << "The c:" << c1 << endl;

  c = fmod(c1, N);

  cout << "Encrypted Message:" << c << endl;

  printf("Public key (N,e) = (%lf,%lld)\n", N, e);

  cout << "The d:" << d << endl;
}

void rsa_decrypt() {

  cout << "Please input c:";

  cin >> c;

  // cout << "Please input N:";

  // cin >> N;
  cout << "Please input d:";
  cin >> d;
  m = pow(c1, d);
  m = fmod(m, N);
 cout << "Original Message is:" << m << endl;
}
int main(int argc, char const *argv[]) {
  int num;
  while (true) {
    cout << "1.RSA encrypt" << endl;
    cout << "2.RSA decrypt" << endl;
    cout << "3.Exit" << endl;
    cout << "Please input a number:";
    cin >> num;
    if (num == 1) {
      rsa_encrypt();
    } else if (num == 2) {
      rsa_decrypt();
    } else {
      cout << "Exit";
      break;
    }
  }

  return 0;
}
