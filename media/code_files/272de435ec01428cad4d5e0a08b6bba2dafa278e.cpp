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

    int infinity = pow(10, 9);

    int wakeup[5];
    int lesson[5];
    int destination[5];

    rep(5) cin >> wakeup[i];
    rep(5) cin >> lesson[i];
    rep(5) cin >> destination[i];

    int s, n, e;

    cin >> s >> n >> e;

    vector<vector<pair<int, int>>> graph(n);

    int first, second, weight;

    rep(e) {
        cin >> first >> second >> weight;
        graph[first].push_back(make_pair(second, weight));
        graph[second].push_back(make_pair(first, weight));
    }

    vector<int> dist(n, infinity), parent(n);
    dist[s] = 0;

    set<pair<int, int>> q;
    q.insert(make_pair(s, dist[s]));

    while (!q.empty()) {
        int v = q.begin()->first;
        q.erase(q.begin());

        for (unsigned int j = 0; j < graph[v].size(); ++j) {
            int to = graph[v][j].first;
            int len = graph[v][j].second;

            if (dist[v] + len < dist[to]) {
                q.erase(make_pair(to, dist[to]));
                dist[to] = dist[v] + len;
                parent[to] = v;
                q.insert(make_pair(to, dist[to]));
            }
        }
    }

    for (int day = 0; day < 5; ++day) {
        if (lesson[day] - wakeup[day] >= dist[destination[day]])
            cout << "Yes " << dist[destination[day]] << endl;
        else cout << "No" << endl;
    }

    return 0;
}

#pragma clang diagnostic pop
