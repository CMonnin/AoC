#include <stdio.h>

#include <stdlib.h>

int comp(const int *a, const int *b) {
        // b-a for descending order
        if (a>b) {
                return *b;
        } else {
                return *a;
        }
}
int process_file(const char* filename){
        FILE *file = fopen(filename, "r");

        if (!file) return 1;

        printf("\n=== Processing %s ===\n", filename);

        char line[256] ;
        int total=0;
                while (fgets(line, sizeof(line), file)) {
                        int arr[100];
                        for (int i=0; i<100; i++) {
                                arr[i]=atoi(&line[i]);
                        }
                        int n = sizeof(arr) / sizeof(arr[0]);
                        for (int i=0; i<100; i++) {
                                printf("%i\n", arr[i]);
                        }
                }

        fclose(file);

        return 0;
}

int main(void)
{
        printf("test.txt  result: %d\n", process_file("test.txt"));
        return 0;
    
}
