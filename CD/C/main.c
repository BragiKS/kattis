#include <stdio.h>
#include <stdlib.h>

int main() {
    int N, M;

    while (1) {
        scanf("%d %d", &N, &M);

        if (N == 0 && M == 0) // Check if input is two zeros
            break; // Exit the loop

        // Read catalog numbers owned by Jack
        int* jack_cds = (int*)malloc(N * sizeof(int));
        for (int i = 0; i < N; i++) {
            scanf("%d", &jack_cds[i]);
        }

        // Read catalog numbers owned by Jill
        int* jill_cds = (int*)malloc(M * sizeof(int));
        for (int i = 0; i < M; i++) {
            scanf("%d", &jill_cds[i]);
        }

        // Count CDs owned by both Jack and Jill
        int count = 0;
        int jack_index = 0, jill_index = 0;
        while (jack_index < N && jill_index < M) {
            if (jack_cds[jack_index] == jill_cds[jill_index]) {
                count++;
                jack_index++;
                jill_index++;
            } else if (jack_cds[jack_index] < jill_cds[jill_index]) {
                jack_index++;
            } else {
                jill_index++;
            }
        }

        printf("%d\n", count);

        free(jack_cds);
        free(jill_cds);
    }

    return 0;
}
