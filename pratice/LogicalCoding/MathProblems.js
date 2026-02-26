function fibonacciSeries(n) {
  let prev1 = 0,
    prev2 = 1,
    current;
  console.log(prev1);
  console.log(prev2);
  for (let i = 2; i <= n; i++) {
    current = prev1 + prev2;
    console.log(current);
    prev1 = prev2;
    prev2 = current;
  }
}

function factorial(n) {
  let fact = 1;

  for (let i = 2; i <= n; i++) {
    fact *= i;
  }
  return console.log(fact);
}

function isPrime(n) {
  let isPrime = true;

  if (n <= 1) return false;

  for (let i = 2; i < n; i++) {
    if (n % i == 0) {
      isPrime = false;
      break;
    }
  }
  return isPrime
    ? console.log("It is a prime number")
    : console.log("It is not a prime number");
}

factorial(5);
isPrime(12);
fibonacciSeries(10);
