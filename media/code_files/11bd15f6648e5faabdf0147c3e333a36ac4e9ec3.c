//#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
const char* Connection(int orbit, int planet) {
	double hippo = sqrt(pow(orbit, 2) + pow(orbit, 2));
	double high = pow(orbit, 2) / hippo;
	if (high != planet) {
		return "Escape";
	}
	return "Trouble";
}
int main() {
	int dist, planet, orbit;
	scanf("%d", &dist);
	scanf("%d", &planet);
	scanf("%d", &orbit);
	printf("%s\n", Connection(orbit, planet));
	return 0;
}