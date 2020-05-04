#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	int n, t;
	cin >> n >> t;
	vector <int> arr(n);
	for(int i = 0; i < n; i++) cin >> arr[i];
	for(int i = 0; i < t; i++){
		int number; cin >> number;
		if(find(arr.begin(), arr.end(), number) != arr.end()){
			cout << "Yes\n";
		}
		else{
			cout << "No\n";
		}
	}	
	
	return 0;
}
