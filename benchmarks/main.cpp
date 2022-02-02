#include <iostream>
#include <time.h>
#include <stdlib.h>
using namespace std;

void hello_world(void){
  cout <<"Hello World" << endl;
}

unsigned int factorial(int n)
{
  if (n <= 1)
  {
    return 1;
  }
  return n * factorial(n - 1);
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


void print_triangle(int size)
{
  for (int i = size; i >= 1; --i)
  {
    for (int j = 1; j <= i; ++j)
    {
      cout << j << " ";
    }
    cout << endl;
  }
}


int main(int argc, char* argv[] )
{
  if(argc == 1){
    cout << "Invalid usage: ./maincpp <choice>" << endl;
    cout << "Choices:" << endl;
    cout << "0. Hello World" << endl;
    cout << "1. Factorial" << endl;
    cout << "2. Sum" << endl;
    cout << "3. Recursive Fibonnaci" << endl;
    cout << "4. Iterative Fibonnaci" << endl;
    cout << "5. Max" << endl;
    cout << "6. Print Triangle" << endl;
    return 1;
  }
  int choice = atoi(argv[1]);
  if(choice > 6 || choice < 0){
    cout << "Invalid choice" << endl;
    return 1;
  }
  double time_spent = 0.0;
  clock_t begin = clock();

  switch(choice){
    case 0:
      hello_world();
      break;
    case 1:
      cout << factorial(20) << endl;
      break;
    case 2:
      cout << sum(1000000) << endl;
      break;
    case 3:
      cout << fib(49) << endl;
      break;
    case 4:
      cout << fib2(49) << endl;
      break;
    case 5:
      cout << max() << endl;
      break;
    case 6:
      print_triangle(100);
      break;
    default:
      cout << "Invalid choice" << endl;
      break;
  }

  clock_t end = clock();

  time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
  cout << "Time spent: " << time_spent << endl;
  return 0;
}
