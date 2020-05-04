#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>
#include <math.h>
#include <ctype.h>


int main11(int argc, char *argv[]) {
    int n, t;
    scanf("%d%d", &n, &t);

    int *a = (int *) calloc(n, sizeof(int));
    int *b = (int *) calloc(t, sizeof(int));
    for (int i = 0; i < n; ++i) {
        scanf("%d", &a[i]);
    }

    for (int i = 0; i < t; ++i) {
        scanf("%d", &b[i]);
    }

    for (int i = 0; i < t; ++i) {
        int f = 0;
        for (int j = 0; j < n; ++j) {
            if (b[i] == a[j])
                f = 1;
        }
        if (f)
            puts("Yes");
        else
            puts("No");
    }
    return 0;
}

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
    int arr1[10000];
    int arr2[10000];
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