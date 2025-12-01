#include <stdio.h>
#include <stdlib.h>

int process_file(const char *filename) {
    FILE *file = fopen(filename, "r");

    int dial = 50;
    int count = 0;
    int prev;
    char dir;
    int number;

    while (fscanf(file, " %c%d", &dir, &number) != EOF) {
        
        if (dir == 'R') {
            dial += number;
        } else {
            dial -= number;
        }
        dial = dial % 100 ;
        if (dial == 0) {
          count++;
        }
        if (dial >= 100) {
          dial -= 100;
          count++;
        }
        if (dial<0 && prev==0) {
          dial+=100;
        }
        if (dial<0 && prev!=0) {
          dial+=100;
        }
        prev = dial; 
    }

    fclose(file);
    return count;
}

int main(void) {
    printf("test.txt  result: %d\n", process_file("test.txt"));
    printf("input.txt result: %d\n", process_file("input.txt"));
    return 0;
}
