#include <stdio.h>
#include <stddef.h>

int main() {
    int n;
    scanf("%d",&n);
    int x;
    for (size_t i = 0; i < n; i++) {
        scanf("%d", &x);
        if (x & 1 == 1) {
            printf("%d is odd\n", x);
        } else {
            printf("%d is even\n", x);
        }
    }
    
}