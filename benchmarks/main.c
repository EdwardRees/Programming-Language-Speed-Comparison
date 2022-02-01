#include <stdio.h>
#include <time.h>
#include <stdlib.h>


void hello_world(void){
  printf("Hello World\n");
}

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

unsigned long fib(int n)
{
  if (n == 0 || n == 1)
  {
    return 1;
  }
  return fib(n - 1) + fib(n - 2);
}

unsigned long fib2(int n)
{
  long f = 0;
  long tl1 = 0;
  long tl2 = 1;
  for (int i = 0; i <= n; i++)
  {
    f = tl1 + tl2;
    if (i % 2 == 0)
    {
      tl1 += tl2;
    }
    else
    {
      tl2 += tl1;
    }
  }
  return f;
}

int max()
{
  int numbers[1000000] = {0};
  for (int i = 0; i < 1000000; i++)
  {
    numbers[i] = (int)(rand() % 1000000);
  }

  int maximum = 0;
  for (int i = 0; i < 1000000; i++)
  {
    if (numbers[i] > maximum)
    {
      maximum = numbers[i];
    }
  }
  return maximum;
}

void print_triangle(int size)
{
  for (int i = size; i >= 1; --i)
  {
    for (int j = 1; j <= i; ++j)
    {
      printf("%d ", j);
    }
    printf("\n");
  }
}

int main(int argc, char* argv[])
{
  if(argc == 1){
    printf("Invalid usage: ./main <choice>\n");
    printf("Choices:\n");
    printf("[0]: hello\n[1]: fact\n[2]: sum\n[3]: recur_fib\n[4]: iter_fib\n[5]: max\n[6]: triangle\n");
    return 1;
  }
  int choice = atoi(argv[1]);
  if(choice > 6 || choice < 0){
    printf("Invalid choice\n");
    return 1;
  }
  srand(time(NULL));
  double time_spent = 0.0;
  clock_t begin = clock();
  switch(choice){
    case 0:
      hello_world();
      break;
    case 1: 
      printf("%lu\n", factorial(20));
      break;
    case 2:
      printf("%d\n", sum(1000000));
      break;
    case 3:
      printf("%lu\n", fib(50));
      break;
    case 4:
      printf("%lu\n", fib2(50));
      break;
    case 5:
      printf("%d\n", max());
      break;
    case 6:
      print_triangle(100);
      break;
    default:
      printf("Invalid choice\n");
      break;
  }
   //printf("%lu\n", factorial(20));
  // printf("%lu\n", fib2(49));
  // printf("%d\n", max());

  clock_t end = clock();

  time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
  printf("Time spent: %f\n", time_spent);

  return 0;
}
