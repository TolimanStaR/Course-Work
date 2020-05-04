#include <stdio.h>
#include <stdlib.h>
const char* Find(int arr[], int searched) {
	int find = 0;
	for (size_t i = 0; arr[i] != 0; i++)
	{
		if (arr[i] == searched) {
			return "Yes";
		}
	}
	return "No";
}
int main() {
	int temp = 0;
	int num_numbers, num_universes;
	scanf("%d", &num_numbers);
	int* arr = (int*)calloc(num_numbers, sizeof(int));
	scanf("%d", &num_universes);
	for (size_t i = 0; i < num_numbers; i++)
	{
		scanf("%d", &arr[i]);
	}
	for (size_t i = 0; i < num_universes; i++)
	{
		scanf("%d", &temp);
		printf("%s\n", Find(arr, temp));
	}
	free(arr);
	return 0;
}