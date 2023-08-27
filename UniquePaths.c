#include <stdlib.h>

int uniquePaths(int m, int n){
    if (m == 1 && n == 1) {
        return 1;
    }
    int* arr = malloc(sizeof(int) * m * n);
    for (int i = 1; i < m; i++) {
        arr[m * 0 + i] = 1;
    }
    for (int j = 1; j < n; j++) {
        arr[m * j + 0] = 1;
    }
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            arr[m * j + i] = arr[m * (j - 1) + i] + arr[m * j + (i - 1)];
        }
    }
    int x = arr[m * (n - 1) + (m - 1)];
    return x;
}
