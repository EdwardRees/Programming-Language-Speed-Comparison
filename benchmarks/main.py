import time
from random import randint
from sys import argv


def helloWorld():
    print("Hello World")


def factorial(n):
    if(n <= 1):
        return 1
    return n * factorial(n - 1)


def sum(n):
    s = 0
    for i in range(n):
        s += i
    return s


def recurFib(n):
    if n <= 1:
        return n
    else:
        return(recurFib(n-1) + recurFib(n-2))


def iterFib(n):
    f = 0
    p1 = 0
    p2 = 1
    for i in range(n + 1):
        f = p1 + p2
        if(i % 2 == 0):
            p1 += p2
        else:
            p2 += p1
    return f


def maxSearch():
    nums = []
    for i in range(1000000):
        nums.append(randint(0, 1000000))
    maximum = 0
    for i in range(len(nums)):
        if(nums[i] > maximum):
            maximum = nums[i]
    return maximum


def printTriangle(size):
    for i in range(size, 1, -1):
        for j in range(1, i):
            print(j, end=" ")
        print()


def main():
    if(len(argv) == 0):
      print("Invalid usage: ./main <choice>\n");
      print("Choices:\n");
      print("[0]: hello\n[1]: fact\n[2]: sum\n[3]: recur_fib\n[4]: iter_fib\n[5]: max\n[6]: triangle\n");
      return
    choice = int(argv[1])
    if(choice > 6 or choice < 0):
        print("Invalid choice")
        return
    start = time.time()
    if(choice == 0):
        helloWorld()
    elif(choice == 1):
        print(factorial(20))
    elif(choice == 2):
        print(sum(1000000))
    elif(choice == 3):
        print(recurFib(50))
    elif(choice == 4):
        print(iterFib(50))
    elif(choice == 5):
        print(maxSearch())
    elif(choice == 6):
        printTriangle(100)
    end = time.time()
    print(f"Time spent: {end - start}")


main()
