#include <stdio.h>
#include <stdlib.h>

long process_file(const char* filename){
        FILE *file = fopen(filename, "r");

        if (!file) return 1;

        printf("\n=== Processing %s ===\n", filename);

        char line[256] ;
        long total=0;
        int count = 1;
                while (fgets(line, sizeof(line), file)) {
                        const int LINE_LEN = 100;
                        int digits = 12;

                        char number_as_string[12 + 1];
                        int pos = 0;  

                        for (int d = 0; d < 12; d++) {
                                char max_char = 0;
                                int max_index = -1;

                                for (int i = pos; i <= LINE_LEN-digits; i++) {
                                        if (line[i] > max_char) {
                                            max_char = line[i];
                                            max_index = i;
                                        }
                                }
                        
                                number_as_string[d] = max_char;
                                pos = max_index + 1;
                                digits--;
                                
                        }
                        
                        number_as_string[12] = '\0';
                        printf("number_as_string %d: %s\n", count, number_as_string);
                        long number_as_int = atol(number_as_string);
                        total += number_as_int;
                        count++;
                }
        fclose(file);
        return total;
}

int main(void)
{
        //printf("test.txt  result: %d\n", process_file("test.txt"));
        printf("input.txt  result: %ld\n", process_file("input.txt"));
        return 0;
    
}
