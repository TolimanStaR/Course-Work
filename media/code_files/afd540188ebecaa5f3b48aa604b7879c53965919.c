#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>
#include <math.h>
#include <ctype.h>


int main(int argc, char *argv[]) {
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
