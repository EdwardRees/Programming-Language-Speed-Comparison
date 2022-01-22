#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void helloWorld(){
  printf("Hello World\n");
}

int main(void){
 double time_spent = 0.0; 
 clock_t begin = clock();
 helloWorld();
 clock_t end = clock();
 time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
 printf("Time spent: %f\n", time_spent);
 return 0;
}

