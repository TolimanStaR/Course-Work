#include <iostream>
#include <cmath>
using namespace std;

int main(){
	int D, Rad, Orb;
	cin >> D >> Rad >> Orb;
	
	double norm_orb = pow(Rad, 2) - pow(double(D) / 2, 2);
	if(norm_orb + 0.00000000001 >= Orb){
		cout << "Escape\n";
	}
	else{
		cout << "Trouble\n";
	}
	
	return 0;
}
