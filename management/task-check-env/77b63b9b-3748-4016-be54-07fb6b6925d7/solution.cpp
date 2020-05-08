#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef map<string, int> dict;

#define fo(i, n) for (int i = 0; i < (n); ++i)
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

    int n, t;
    cin >> n >> t;
    auto a = new int[n];
    auto y = new int[t];

    fo(i, n) cin >> a[i];
    fo(i, t) cin >> y[i];

    stable_sort(a, a + n);

    fo(i, t) cout << (binary_search(a, a + n, y[i]) ? "Yes" : "No") << endl;

    return 0;
}

#pragma clang diagnostic pop

