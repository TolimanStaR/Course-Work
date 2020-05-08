#include <bits/stdc++.h>

using namespace std;

#define rep(x) for(int i = 0; i < x; ++i)

int main() {

     int n, s;
     int up[5];
     int lesson[5];
     int hse_num[5];
     int dp[100][100];

     rep(5)cin >> up[i];
     rep(5)cin >> lesson[i];
     rep(5)cin >> hse_num[i];
     cin >> n >> s;
     rep(n)for (int j = 0; j < n; ++j)
               cin >> dp[i][j];

     for (int k = 0; k < n; ++k) {
          for (int i = 0; i < n; ++i) {
               for (int j = 0; j < n; ++j) {
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
               }
          }
     }

     rep(5) {
          if (dp[s - 1][hse_num[i] - 1] <= lesson[i] - up[i]) {
               cout << "Yes " << dp[s - 1][hse_num[i] - 1] << endl;
          } else cout << "No" << endl;
     }


     return 0;
}