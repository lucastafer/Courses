// 1) Functions without return

function withoutReturn(): void {
  console.log("This function has no return!");
}

// 2) Callback as argument

function greeting(name: string): string {
  return `Hi ${name}!`;
}

function preGreeting(f: (name: string) => string, userName: string) {
  console.log("Preparing function!");

  const greet = f(userName);

  console.log(greet);
}

preGreeting(greeting, "Lucas");

// 3) generic function

function firstElement<T>(arr: T[]): T {
  return arr[0];
}

console.log(firstElement([1, 2, 3]));

function mergeObjects<U, T>(obj1: U, obj2: T) {
  return {
    ...obj1,
    ...obj2,
  };
}

const newObject = mergeObjects(
  { name: "Lucas" },
  { age: 21, job: "Developer" }
);

console.log(newObject);

// 4) constraints

function biggestNumber<T extends number | string>(a: T, b: T) {
  let biggest: T;

  if (+a > +b) {
    biggest = a;
  } else {
    biggest = b;
  }

  return biggest;
}

console.log(biggestNumber(5, 3));
console.log(biggestNumber("12", "4"));

// 5) specify argument type

function mergeArrays<T>(arr1: T[], arr2: T[]) {
  return arr1.concat(arr2);
}

console.log(mergeArrays<number | string>([1, 2, 3], ["Test", "Testing"]));

//Use this method when the code is already done, and you can't change it. However, when you are starting from bottom, create constraints as anterior class.

// 6) optional arguments

const modernGreeting = (name: string, greet?: string) => {
  if (greet) {
    return `Hi ${greet} ${name}.`;
  }
  return `Hi ${name}`;
};

console.log(modernGreeting("Lucas"));
console.log(modernGreeting("Lucas", "Dr."));

// 7) Default arguments

function sumDefault(n: number, m = 10) {
  return n + m;
}

console.log(sumDefault(5));
console.log(sumDefault(10, 8));

// 8) unknown type

function doSomething(x: unknown) {
  if (Array.isArray(x)) {
    console.log(x[0]);
  } else if (typeof x === "number") {
    console.log("X é um número!");
  }
}

doSomething([1, 2, 3]);
doSomething(5);

// 9) never type



// 10) Rest operator

function sumAll(...n: number[]) {
  return n.reduce((number, sum) => sum + number);
}

console.log(sumAll(1, 2, 3, 4, 5));
console.log(sumAll(5, 348, 2348));


// 11) Destructuring as argument

function showProductDetails({name, price}: {name: string, price: number}): string {
    return `O nome do produto é ${name} e ele custa R$${price}.`
}

const shirt = {name: "T-Shirt", price: 29.90}
console.log(showProductDetails(shirt))
