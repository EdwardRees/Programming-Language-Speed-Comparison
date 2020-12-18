#include <stdio.h>
#include <time.h>
#include <stdlib.h>

unsigned int sum(int n)
{
  unsigned int s = 0;
  for (int i = 0; i < n; i++)
  {
    s += i;
  }
  return s;
}

unsigned long factorial(int n)
{
  if (n <= 1)
  {
    return 1;
  }
  return n * factorial(n - 1);
}

unsigned long fib(int n){
  if(n == 0 || n == 1){
    return 1;
  }
  return fib(n - 1) + fib(n - 2);
}

unsigned long fib2(int n){
  long f =0;
  long tl1 = 0;
  long tl2 = 1;
  for(int i=0; i<=n; i++){
    f = tl1 + tl2;
    if(i % 2 == 0 ){
      tl1 += tl2;
    } else {
      tl2 += tl1;
    }
  }
  return f;
}

int max(){
  srand(time(NULL));
  int numbers[1000000] = {0};
  for(int i = 0; i<1000000; i++){
    numbers[i] = (int)(rand() % 1000000);
  }

  int maximum = 0;
  for(int i=0; i<1000000; i++){
    if(numbers[i] > maximum){
      maximum = numbers[i];
    }
  }
  return maximum;
}


int main(void)
{
  double time_spent = 0.0;
  clock_t begin = clock();

  // printf("%lu\n", fib2(49));
  printf("%d\n", max());

  clock_t end = clock();

  time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
  printf("Time spent: %f\n", time_spent);

  return 0;
}