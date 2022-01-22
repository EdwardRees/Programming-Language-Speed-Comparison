const helloWorld = () => {
  console.info("Hello World");
}
const factorial = (n) => {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
};

const sum = (n) => {
  let s = 0;
  for (let i = 0; i < n; i++) {
    s += i;
  }
  return s;
};

const fib1 = (n) => {
  if (n == 0 || n == 1) {
    return 1;
  }
  return fib1(n - 1) + fib1(n - 2);
};
const fib2 = (n) => {
  let f =0;
  let tl1 = 0;
  let tl2 = 1;
  for(let i=0; i<=n; i++){
    f = tl1 + tl2;
    if(i % 2 == 0 ){
      tl1 += tl2;
    } else {
      tl2 += tl1;
    }
  }
  return f;
}

const maxSearch = () => {
  let nums = [];
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

const printTriangle = (size) => {
  for(let i=size; i>=1; i--){
    for(let j=1; j<=i; j++){
      process.stdout.write(j + " ");
    }
    console.log();
  }
}

const main = () => {
  console.time("fib1");
  printTriangle(100);
  console.timeEnd("fib1");
  // console.time("factorial");
  // console.info(factorial(10));
  // console.timeEnd("factorial");
  // sum(1000000);
};

main();
