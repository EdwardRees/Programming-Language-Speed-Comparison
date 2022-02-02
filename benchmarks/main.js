const helloWorld = () => {
  console.info("Hello World");
};
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
  let f = 0;
  let tl1 = 0;
  let tl2 = 1;
  for (let i = 0; i <= n; i++) {
    f = tl1 + tl2;
    if (i % 2 == 0) {
      tl1 += tl2;
    } else {
      tl2 += tl1;
    }
  }
  return f;
};

const maxSearch = () => {
  let nums = [];
  for (let i = 0; i < 1000000; i++) {
    nums.push(Math.random() * 1000000);
  }
  let maximum = 0;
  for (let i = 0; i < 1000000; i++) {
    if (maximum < nums[i]) {
      maximum = nums[i];
    }
  }
  return maximum;
};

const printTriangle = (size) => {
  for (let i = size; i >= 1; i--) {
    for (let j = 1; j <= i; j++) {
      process.stdout.write(j + " ");
    }
    console.log();
  }
};

const main = () => {
  let args = process.argv;
  if (args.length < 3) {
    console.info("Invalid usage: node main.js <choice>\n");
    console.info("Choices:\n");
    console.info(
      "[0]: hello\n[1]: fact\n[2]: sum\n[3]: recur_fib\n[4]: iter_fib\n[5]: max\n[6]: triangle\n"
    );
    return;
  }
  let action = parseInt(args[2]);
  if (action < 0 || action > 6) {
    console.info("Invalid choice\n");
    return;
  }

  let actionName = action == 0 ? "hello" : action == 1 ? "fact" : action == 2 ? "sum" : action == 3 ? "recur_fib" : action == 4 ? "iter_fib" : action == 5 ? "max" : "triangle";
  console.time("Time spent");
  switch (action) {
    case 0:
      helloWorld();
      break;
    case 1:
      console.info(factorial(20));
      break;
    case 2:
      console.info(sum(1000000));
      break;
    case 3:
      console.info(fib1(50));
      break;
    case 4:
      console.info(fib2(50));
      break;
    case 5:
      console.info(maxSearch());
      break;
    case 6:
      printTriangle(100);
      break;
    default:
      console.info("Invalid choice\n");
      break;
  }

  console.timeEnd("Time spent");
  // console.time("factorial");
  // console.info(factorial(10));
  // console.timeEnd("factorial");
  // sum(1000000);
};

main();
