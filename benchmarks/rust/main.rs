#![allow(dead_code, unused_variables, unused_mut, unused_unsafe, unused_variables)]
use std::time::{Instant};
use rand::Rng;
use std::env;

fn hello_world() {
    println!("Hello World");
}

fn sum(n: i32) -> i32 {
    let mut s = 0;
    for i in 0..n {
        s += i;
    }
    return s;
}

fn fact(n: i64) -> i64 {
    if n <= 1 {
        return 1;
    }
    return n * fact(n - 1);
}

fn fib(n: i64) -> i64 {
    if n < 3 {
        return 1;
    }
    return fib(n - 1) + fib(n - 2);
}

fn fib2(n: i32) -> i64 {
    let mut f = 0;
    let mut tl1 = 0;
    let mut tl2 = 1;
    for i in 0..n - 1 {
        f = tl1 + tl2;
        if i % 2 == 0 {
            tl1 += tl2;
        } else {
            tl2 += tl1;
        }
    }
    return f;
}

fn max() -> i32 {
    let mut l = Vec::new();
    let mut rng = rand::thread_rng();
    for i in 0..1000000 {
        l.push(rng.gen_range(0..1000000));
    }
    let mut max = 0;
    for i in 0..1000000 {
        if l[i] > max {
            max = l[i];
        }
    }
    return max;
}

fn print_triangle(size: i32) {
    // for loop from size to 0
    for i in (0..size).rev() {
        // for loop from 0 to i
        for j in 0..i {
            print!("{} ", j + 1);
        }
        println!("");
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let n = args[1].parse::<i32>().unwrap();
    let now = Instant::now();
    match n {
        0 => hello_world(),
        1 => println!("{}", fact(20)),
        2 => println!("{}", sum(1000000)),
        3 => println!("{}", fib(49)),
        4 => println!("{}", fib2(48)),
        5 => println!("{}", max()),
        6 => print_triangle(100),
        _ => println!("{}", "Invalid input"),
    }
  println!("Time spent: {}", now.elapsed().as_nanos());
}
