#include <stdio.h>
#include <stdlib.h>

int process_file(const char* filename){
        FILE *file = fopen(filename, "r");

        if (!file) return 1;

        printf("\n=== Processing %s ===\n", filename);

        char line[256] ;
        int total=0;
        int count = 1;
                while (fgets(line, sizeof(line), file)) {
                        char first = line[0];
                        int first_index = 0;
                        char second = 0;
                        int second_index= 0;
                        for (int i=1; i<99; i++) {
                                if (first < line[i]) {
                                        first = line[i];
                                        first_index = i;
                                }
                        }
                        for (int j=first_index+1; j<100; j++) {
                                if (second< line[j]) {
                                        second = line[j];
                                        second_index= j;
                                }
                        }
                        char number_as_string[3];
                        number_as_string[0] = first;
                        number_as_string[1] = second;
                        number_as_string[2] = '\0';

                        printf("number_as_string: %d: %s\n",count, number_as_string);

                        int number_as_int = atoi(number_as_string);
                        total += number_as_int;
                        count++;

                        }

        fclose(file);

        return total;
}

int main(void)
{
        //printf("test.txt  result: %d\n", process_file("test.txt"));
        printf("input.txt  result: %d\n", process_file("input.txt"));
        return 0;
    
}
