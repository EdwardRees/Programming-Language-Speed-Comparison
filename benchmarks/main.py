import time
from random import randint


def helloWorld():
    print("Hello World")


def factorial(n):
    if(n <= 1):
        return 1
    return n * factorial(n - 1)


def sum(n):
    start = time.time()
    s = 0
    for i in range(n):
        s += i
    end = time.time()
    print(f"{end - start}")
    return s


def recurFib(n):
    if n <= 1:
        return n
    else:
        return(recurFib(n-1) + recurFib(n-2))
    # if(n <= 1):
    #   return 1
    # else:
    #   print(n)
    #   return recurFib(n - 1) + recurFib(n - 2)


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
    start = time.time()
    printTriangle(100)
    end = time.time()
    print(f"{end - start}")


main()
