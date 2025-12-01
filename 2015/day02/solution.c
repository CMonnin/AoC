#include <stdio.h>
#include <stdlib.h>


void bubble_sort(int array[], int array_len) {
    for (int i = 0; i < array_len - 1; i++) {
        for (int j = 0; j < array_len - 1 - i; j++) {
            if (array[j] > array[j + 1]) {
                int tmp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = tmp;
            }
        }
    }
}

int main(void) {
  long long total = 0;
  long long total_with_ribbon =0;
  int l,w,h,a,b,c;
  while (scanf("%dx%dx%d",&l, &w, &h)==3) {
    int arr[] = {l,w,h};
    int slack =0;
    a = l*w;
    b = w*h;
    c = h*l;
    bubble_sort(arr, sizeof(arr)/sizeof(arr[0]));
    for (int i=0; i<2; i++) {
      total_with_ribbon += 2*arr[i];
    }
    slack = arr[0]*arr[1];
    total = total+2*(a+b+c)+slack;
    total_with_ribbon = (total_with_ribbon+(l*w*h));

  }
  printf("%lld total part1\n",total);
  printf("%lld total part2\n",total_with_ribbon);
  return EXIT_SUCCESS;
}

