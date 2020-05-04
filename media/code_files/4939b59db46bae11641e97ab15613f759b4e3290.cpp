#include <iostream>
#include <cmath>
using namespace std;

int main(){
	int D, Rad, Orb;
	cin >> D >> Rad >> Orb;
	
	double norm_rad = sqrt(pow(Orb, 2) - pow(double(D) / 2, 2));
	if(norm_rad + 0.00000000001 >= Rad){
		cout << "Escape\n";
	}
	else{
		cout << "Trouble\n";
	}
	
	return 0;
}
