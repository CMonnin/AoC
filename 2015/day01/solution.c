#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(void) {
  int level = 0;
  int c;
  int position = 0;
  bool position_reached = false;

  while ((c = getchar()) != EOF) {
    ++position;
    if (c == '(') {
      ++level;
    } else {
      --level;
    }
    if (level == -1 && position_reached == false) {
      printf("%d\n", position);
      position_reached = true;
    }
  }
  printf("%d\n", level);
  return EXIT_SUCCESS;
}
