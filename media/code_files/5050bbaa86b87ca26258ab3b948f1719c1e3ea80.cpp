#include <stdio.h>
#include <math.h>
#include <malloc.h>

int printfAnswer(int found, int size, int* arr1) {
	for (int i = 0; i < size; i++) {
		if (arr1[i] == found) {
			return 1;
		}
	}
	return 0;
}

int main() {
	int  n, k;
	scanf("%d", &n);
	scanf("%d", &k);
	int arr1[100];
	int arr2[100];
	for (int i = 0; i < n; i++) 
		scanf("%d", &arr1[i]);
	

	for (int i = 0; i < k; i++) {
		scanf("%d", &arr2[i]);
		if (printfAnswer(arr2[i], n, arr1) == 1) 
			printf("Yes\n");
		else
			printf("No\n");
	}
	
	return 0;
}