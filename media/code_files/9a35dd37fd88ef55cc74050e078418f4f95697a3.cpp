#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef map<string, int> dict;

#define fo(i, n) for (int i = 0; i < (n); ++i)
#define rep(x) for (int i = 0; i < (x); ++i)
#define pb push_back
#define fi first
#define se second

void optimization() {
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios_base::sync_with_stdio(false);
}

#pragma clang diagnostic push
#pragma ide diagnostic ignored "cert-msc51-cpp"
#pragma ide diagnostic ignored "cert-msc30-c"


int main() {
    optimization();

    int n;
    cin >> n;

    string s;
    cin >> s;

    auto prefix = new char[n];
    prefix[0] = (char) s[0];

    for (int i = 1; i < n; ++i)
        prefix[i] = min(prefix[i - 1], (char) s[i - 1]);

    for (int i = 0; i < n; ++i) {
        if (prefix[i] >= (char) s[i]) {
            cout << "A" << endl;
        } else cout << "H" << endl;
    }

    return 0;
}

#pragma clang diagnostic pop
