#include <bits/stdc++.h>
#include <vector>
using namespace std;
vector<int> nums(4, 0);
vector<char> ch(3);
int main(int argc, char const *argv[]) {
  while (cin >> nums[0] >> ch[0] >> nums[1] >> ch[1] >> nums[2] >> ch[2] >>
         nums[3]) {
    if (ch[0] == '.' && ch[1] == '.' && ch[2] == '.') {
      if (nums[0] >= 0 && nums[0] <= 255 && nums[1] >= 0 && nums[1] <= 255 &&
          nums[2] >= 0 && nums[2] <= 255 && nums[3] >= 0 && nums[3] <= 255) {
        cout << "YES" << endl;
      } else {
        cout << "NO" << endl;
      }
    } else {
      cout << "NO" << endl;
    }
  }
  return 0;
}
