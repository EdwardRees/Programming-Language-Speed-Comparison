public class Main {
  public static void helloWorld(){
    System.out.println("Hello World");
  }
  public static long factorial(int n) {
    if (n <= 1) {
      return 1;
    }
    return n * factorial(n - 1);
  }

  public static long sum(int n) {
    long start = System.nanoTime();
    int s = 0;
    for (int i = 0; i < n; i++) {
      s += i;
    }
    long end = System.nanoTime();
    return (end - start);
  }

  public static long fib(int n) {
    if (n == 0 || n == 1) {
      return 1;
    }
    return fib(n - 1) + fib(n - 2);
  }

  public static long fib2(int n) {
    long f = 0;
    long tempLast1 = 0;
    long tempLast2 = 1;
    for (int i = 0; i <= n; i++) {
      f = tempLast1 + tempLast2;
      if (i % 2 == 0) {
        tempLast1 += tempLast2;
      } else {
        tempLast2 += tempLast1;
      }
    }
    return f;
  }

  public static int max(){
    int[] numbers = new int[1000000];
    for(int i=0; i<1000000; i++){
      numbers[i] = (int)(Math.random() * 1000000);
    }
    int maximum = 0;
    for(int i=0; i<1000000; i++){
      if(maximum < numbers[i]){
        maximum = numbers[i];
      }
    }
    return maximum;
  }

  public static void print_triangle(int size){

  for (int i = size; i >= 1; --i)
  {
    for (int j = 1; j <= i; ++j)
    {
      System.out.printf("%d ", j);
    }
    System.out.printf("\n");
  }

}

  public static void main(String[] args) {
    long start = System.nanoTime();
    helloWorld();
    // System.out.println(max());
    long end = System.nanoTime();
    System.out.println(end - start);

  }
}