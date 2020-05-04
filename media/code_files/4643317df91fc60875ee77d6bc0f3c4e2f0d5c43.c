//#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
const char* Connection(int orbit, int planet, int dist) {
	double high = sqrt(pow(orbit, 2) - pow((dist / 2), 2));
	if (high > (double)planet) {
		return "Escape";
	}
	else return "Trouble";
}
int main() {
	int dist, planet, orbit;
	scanf("%d", &dist);
	scanf("%d", &planet);
	scanf("%d", &orbit);
	printf("%s\n", Connection(orbit, planet, dist));
	return 0;
}