#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int check_halves(char *str) {
    int len = strlen(str);
    int mid = len / 2;
    
    if (strncmp(str, str + mid, mid) == 0) {
      return 0;
    } else {
      return 1;
    }
}

int is_even(int len) {
    // also checks that len > 1
    if (len%2==0) {
      return 0;
    } else {
      return 1;
    }
}

int compare(char* str) {
    int len = strlen(str);
    int* factors = malloc(len * sizeof(int)); 
    int count = 0;
    
    for (long i = 1; i < len; i++) {
        if (len % i == 0) {
            factors[count++] = i;
        }
    }
    
    if (count == 0) {  
        free(factors);
        return 0;
    }
    
    factors = realloc(factors, count * sizeof(int));
    
    for (int i = 0; i < count; i++) {
        int pattern_len = factors[i];
        
        char* pattern = malloc(pattern_len + 1);
        strncpy(pattern, str, pattern_len);
        pattern[pattern_len] = '\0';
        
        int repetitions = len / pattern_len;
        char* reconstructed = malloc(len + 1);
        reconstructed[0] = '\0';
        
        for (int j = 0; j < repetitions; j++) {
            strcat(reconstructed, pattern);
        }
        
        if (strcmp(str, reconstructed) == 0) {
            free(pattern);
            free(reconstructed);
            free(factors);
            return 1;
        }
        
        free(pattern);
        free(reconstructed);
    }
    
    free(factors);
    return 0;
}



long process_file(const char *filename) {
  FILE *file = fopen(filename, "r");
  if (!file) return 1;

  
  printf("\n=== Processing %s ===\n", filename);
  char *line = NULL;
  size_t len = 0;
  char array[1024][256];
  int size = 0;
  long total=0;
  int count= 0;

  if (getline(&line, &len, file) != -1) {
    char *str_pt1, *str_pt2;
    char *token = strtok_r(line, ",", &str_pt1);
    while (token!= NULL) {
      char *numbers = strtok_r(token,"-",&str_pt2);
      while (numbers!= NULL) {
          char *num = numbers;
          printf("%s\n", num);
          strncpy(array[size], num, 255);
          array[size][255] = '\0';
          size++;
          numbers = strtok_r(NULL, "-",&str_pt2);
      }
      token = strtok_r(NULL,",",&str_pt1);
    }
  }
  char *str1, *str2;
  for (int i=0;i<size;i++) {
    if (i%2==0) {
      str1=array[i];
    // printf("%s\n","str1");
    // printf("%s\n",str1);
    }else {
      str2=array[i];
    // printf("%s\n","str2");
    // printf("%s\n",str2);
      long range_end = atol(str2)+1;
      for (long j=atol(str1); j<range_end; j++) {
        char current_num[256];
        sprintf(current_num,"%ld",j);
        if (strlen(current_num)%2==0) {
          if (check_halves(current_num)==0 ){
            printf("%s\n",current_num);
            total+=atol(current_num);
            printf("%s%ld\n","current total: ",total);
            count++;
          }
        }
      }
    }
  }
  free(line);
  fclose(file);
  printf("%s%d\n","count: ",count);
  return total;
}


int main(void) {
    printf("test.txt  result: %ld\n", process_file("test.txt"));
    printf("input.txt result: %ld\n", process_file("input.txt"));
    return 0;
}
