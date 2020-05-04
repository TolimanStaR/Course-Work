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


ll tree[400000];

void build(int a[], int v, int tree_left, int tree_right) {
    if (tree_left == tree_right)
        tree[v] = a[tree_left];
    else {
        int tree_middle = (tree_left + tree_right) / 2;
        build(a, v * 2, tree_left, tree_middle);
        build(a, v * 2 + 1, tree_middle + 1, tree_right);
        tree[v] = tree[v * 2] + tree[v * 2 + 1];
    }
}


ll dist_sum(int v, int tree_left, int tree_right, int left, int right) {
    if (left > right)
        return 0;

    if (left == tree_left and right == tree_right)
        return tree[v];

    int tree_middle = (tree_left + tree_right) / 2;
    return (
            dist_sum(v * 2, tree_left, tree_middle, left, min(right, tree_middle)) +
            dist_sum(v * 2 + 1, tree_middle + 1, tree_right, max(left, tree_middle + 1), right)
    );
}


void update(int v, int tree_left, int tree_right, int pos, int new_val) {
    if (tree_left == tree_right)
        tree[v] = new_val;
    else {
        int tree_middle = (tree_left + tree_right) / 2;
        if (pos <= tree_middle)
            update(v * 2, tree_left, tree_middle, pos, new_val);
        else
            update(v * 2 + 1, tree_middle + 1, tree_right, pos, new_val);
        tree[v] = tree[v * 2] + tree[v * 2 + 1];
    }
}


int main() {
    optimization();

    int n, t;
    cin >> n >> t;

    auto a = new int [n];
    rep(n) cin >> a[i];

    build(a, 1, 0, n - 1);

    rep(4 * n) cout << tree[i] << ' ';

    for (int i = 0; i < t; ++i) {
        int request;
        cin >> request;
        if (request) {
            int left, right;
            cin >> left >> right;
            cout << dist_sum(1, 0, n - 1, left, right) << ' ';
        } else {
            int pos, value;
            cin >> pos >> value;
            update(1, 0, n - 1, pos, value);
        }
    }

    return 0;
}

#pragma clang diagnostic pop
