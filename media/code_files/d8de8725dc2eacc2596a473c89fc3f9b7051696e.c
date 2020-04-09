#include <stdio.h>
#include <stdlib.h>

int main () {
	int n, k, ans;
	scanf("%d%d", &n, &k);
	int* a = (int*) calloc(n, sizeof(int));
	for (int i = 0; i < n; ++i) 
		scanf("%d", &a[i]);

	for (int i = 0; i < n; ++i)
		a[i] == k ? ans = 1 : ans;

	puts(ans == 1 ? "Yes" : "No");

	return 0;
}
