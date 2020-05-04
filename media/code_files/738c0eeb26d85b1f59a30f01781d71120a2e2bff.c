#include <stdio.h>
int Sum(int a, int b) {
	return a + b;
}
int main() {
	int a, b;
	scanf("%d", &a);
	scanf("%d", &b);
	printf("%d", Sum(a, b));
}