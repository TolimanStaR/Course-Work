#include <stdio.h>
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
	int arr[1000] = { 0 };
	int temp = 0;
	int num_numbers, num_universes;
	scanf("%d", &num_numbers);
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
}