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
unsigned long long process_file(const char *filename) {
  FILE *file = fopen(filename, "r");
  if (!file) return 1;

  
  printf("\n=== Processing %s ===\n", filename);
  char *line = NULL;
  size_t len = 0;
  char array[1024][256];
  int size = 0;
  unsigned long long total=0;
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
      for (int j=atoi(str1); j<atoi(str2)+1; j++) {
        char current_num[256];
        sprintf(current_num,"%d",j);
        if (strlen(current_num)%2==0) {
          if (check_halves(current_num)==0 ){
            printf("%s\n",current_num);
            total+=atoi(current_num);
            printf("%s%llu\n","current total",total);
            count++;
          }
        }
      }
    }
  }
  free(line);
  fclose(file);
  printf("%s%d\n","count:",count);
  return total;
}


int main(void) {
    printf("test.txt  result: %llu\n", process_file("test.txt"));
    printf("input.txt result: %llu\n", process_file("input.txt"));
    return 0;
}
