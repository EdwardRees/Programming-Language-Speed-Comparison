const helloWorld = (): void => {
  console.info("Hello World");
}
const factorial = (n: number): number => {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
};

const sum = (n: number): number => {
  console.time("sum");
  let s = 0;
  for (let i = 0; i < n; i++) {
    s += i;
  }

  console.timeEnd("sum");
  return s;
};

const fib1 = (n: number): number => {
  if (n == 0 || n == 1) {
    return 1;
  }
  return fib1(n - 1) + fib1(n - 2);
};
const fib2 = (n: number): number => {
  let f: number = 0;
  let tl1: number = 0;
  let tl2: number = 1;
  for (let i: number = 0; i <= n; i++) {
    f = tl1 + tl2;
    if (i % 2 == 0) {
      tl1 += tl2;
    } else {
      tl2 += tl1;
    }
  }
  return f;
};

const maxSearch = () : number => {
  let nums:Array<number> = [];
  for(let i=0; i<1000000; i++){
    nums.push((Math.random() * 1000000));
  }
  let maximum = 0;
  for(let i=0; i<1000000; i++){
    if(maximum < nums[i]){
      maximum = nums[i];
    }
  }
  return maximum;
}



const printTriangle = (size: number): void => {
  for(let i=size; i>=1; i--){
    for(let j=1; j<=i; j++){

      console.info(j);
    }
  }
}
const main = () => {
  // console.log(sum(1000000));
  console.time("printTriangle");
  // helloWorld();
  printTriangle(100);
  console.timeEnd("printTriangle");
};

main();

export {};
