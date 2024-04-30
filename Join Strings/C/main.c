#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stddef.h>

typedef struct Node {
    char *data;
    struct Node *next;
    struct Node *tail;
} node_t;

// Get line from the std input.
char *fetchline(void) {
    char *line = malloc(120); // Initial buffer size
    char *linep = line;
    size_t lenmax = 100, len = lenmax;
    int c;

    if (line == NULL)
        return NULL;

    for (;;) {
        c = fgetc(stdin);
        if (c == EOF || c == '\n') {
            *line = '\0'; // Replace newline with null terminator
            break;
        }

        if (--len == 0) {
            len = lenmax;
            char *linen = realloc(linep, lenmax *= 2);
            if (linen == NULL) {
                free(linep);
                return NULL;
            }
            line = linen + (line - linep);
            linep = linen;
        }

        *line++ = c;
    }
    return linep;
}




// Add input strings to list
void add_data(node_t *node) {
    node->data = fetchline();
    node->next = NULL;
    node->tail = node;
}

// Connect nodes
void connect(node_t *l1, node_t *l2) {
    l1->tail->next = l2;
    l1->tail = l2->tail;
}

// print the connected list
void print(node_t *list) {
    while (list != NULL) {
        printf("%s", list->data);
        list = list->next;
    }
    // Goto nextline after all the printing
    putchar('\n');
}

int main() {
    int N = 0;
    scanf("%d", &N);
    getchar();
    node_t *list = malloc(N * sizeof(node_t));

    for (size_t i = 0; i < N; i++) {
        add_data(&list[i]);
    }

    int a = 0, b = 0;
    for (size_t i = 0; i < N-1; i++) {
        scanf("%d %d", &a, &b);
        a--; b--;
        connect(&list[a], &list[b]);
    }
    
    print(&list[a]);
    
    free(list);
    return 0;
}