#include <bits/stdc++.h>
using namespace std;

int main () {
	int n, t;
	cin >> n >> t;
	auto *a = new int [n];
	auto *s = new pair<int, int>[t];
	
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	
	for (int i = 0; i < t; ++i)
		cin >> s[i].first >> s[i].second;
	
	auto pref = new int [n];
	pref[0] = a[0];
	
	for (int i = 1; i < n; ++i)
		pref[i] = pref[i - 1] + a[i];
	
	for (int i = 0; i < t; ++i)
		cout << pref[s[i].second] - pref[s[i].first] << endl;
	
	
	return 0;
}
