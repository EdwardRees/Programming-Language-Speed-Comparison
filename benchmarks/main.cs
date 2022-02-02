using System;
namespace programminglanguagespeedtest {

  class CSTest {

    static void HelloWorld(){
      Console.WriteLine("Hello World");
    }

    static ulong Factorial(ulong n){
      if(n <= 1){
        return 1;
      }
      return n * Factorial(n - 1);
    }

    static uint Summation(int n){
      uint s = 0;
      for(uint i=0; i<n; i++){
        s += i;
      }
      return s;
    }

    static ulong Fibonacci(uint n){
      if(n <= 1){
        return 1;
      }
      return Fibonacci(n - 1) + Fibonacci(n - 2);
    }

    static long Fibonacci2(int n){
      long f = 0;
      long tl1 = 0;
      long tl2 = 1;
      for(int i=0; i<=n; i++){
        f = tl1 + tl2;
        if(i % 2 == 0){
          tl1 += tl2;
        } else {
          tl2 += tl1;
        }
      }
      return f;
    }

    static long MaxSearch(int n){
      int[] nums = new int[n];
      Random rand = new Random();
      for(int i=0; i<n; i++){
        nums[i] = rand.Next(1, 1000000);
      }
      int max = 0;
      for(int i=0; i<n; i++){
        if(max < nums[i]){
          max = nums[i];
        }
      }
      return max;
    }

    static void Triangle(int size){
      for(int i=size; i>=1; i--){
        for(int j=1; j<=i; j++){
          Console.Write(j);
          Console.Write(" ");
        }
        Console.WriteLine();
      }
    }

    static void Main(string[] args){
      if(args.Length == 0){
        Console.WriteLine("Usage: main.cs <benchmark>");
        Console.WriteLine("Choices:");
        Console.WriteLine("[0]: hello\n[1]: fact\n[2]: sum\n[3]: recur_fib\n[4]: iter_fib\n[5]: max\n[6]: triangle\n");
        return;
      }
      int choice = int.Parse(args[0]);
      if(choice > 6 || choice < 0){
        Console.WriteLine("Invalid choice");
        return;
      }

      var watch = System.Diagnostics.Stopwatch.StartNew();
      // the code that you want to measure comes here
      switch(choice){
        case 0:
          HelloWorld();
          break;
        case 1:
          Console.WriteLine(Factorial(20));
          break;
        case 2:
          Console.WriteLine(Summation(1000000));
          break;
        case 3:
          Console.WriteLine(Fibonacci(49));
          break;
        case 4:
          Console.WriteLine(Fibonacci2(49));
          break;
        case 5:
          Console.WriteLine(MaxSearch(1000000));
          break;
        case 6:
          Triangle(100);
          break;
      }
      watch.Stop();
      var ts = watch.Elapsed;
      var elapsedString = String.Format("{0:00},{1:00}.{2:000}",
            ts.Minutes,
            ts.Seconds,
            ts.Milliseconds);
      Console.WriteLine("Time spent: " + elapsedString);

    }
  }
}
