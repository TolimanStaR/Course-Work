#include <iostream>
using namespace std;

int main () {
	int n, k, ans;
	cin >> n >> k;
	auto a = new int [n];
	for (int i = 0; i < n; ++i) 
		cin >> a[i];

	for (int i = 0; i < n; ++i)
		a[i] == k ? ans = 1 : ans = 0;

	cout << (ans == 1 ? "Yes" : "No");
	return 0;
}