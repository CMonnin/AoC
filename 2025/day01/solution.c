#include <stdio.h>

int process_file(const char *filename) {
    FILE *file = fopen(filename, "r");
    int dial = 50;
    int count = 0;
    int prev;
    char dir;
    int number;
    
    printf("\n=== Processing %s ===\n", filename);
    printf("Starting dial position: %d\n\n", dial);
  
    while (fscanf(file, " %c%d", &dir, &number) != EOF) {
            prev = dial;
            
            if (dir == 'R') {
                dial = (dial+number+100)%100;
//                printf("Rotation: R%d (dial: %d + %d = %d)\n", number, prev, number, dial);
                for (int i=1; i<number; i++) {
                  int tmp = 0;
                  tmp = prev+i;
                  if (tmp ==0 || tmp%100==0) {
                    count++;
                  }
                }
            } else if (dir == 'L') {
                dial = (dial-number+100)%100;
                // printf("Rotation: L%d (dial: %d - %d = %d)\n", number, prev, number, dial);
                for (int i=1; i<number; i++) {
                  int tmp = 0;
                  tmp = prev-i;
                  if (tmp==0 || tmp%100== 0) {
                    count++;
                  }
                }
            }

            if (dial == 0) {
              count++;
              // printf("  Landed on 0 (count++)\n");
            }
            
            // printf("  Final position: %d, Total count so far: %d\n\n", dial, count);
        }
    
    fclose(file);
    printf("=== Final count for %s: %d ===\n\n", filename, count);
    return count;
}

int main(void) {
    printf("test.txt  result: %d\n", process_file("test.txt"));
    printf("input.txt result: %d\n", process_file("input.txt"));
    return 0;
}
