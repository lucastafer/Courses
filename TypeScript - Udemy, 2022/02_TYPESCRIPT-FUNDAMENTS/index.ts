// 1- Number

let x: number = 10;
console.log(typeof x);
console.log(x);

x = 15;
console.log(x);

const y: number = 15.5555;
console.log(y.toFixed(2));
console.log(y.toPrecision(3));

// 2- String

const firstName: string = "Lucas";
console.log(firstName);

let lastName: string = "Tafer";

const fullName = firstName + " " + lastName;
console.log(fullName);
console.log(typeof fullName);

// 3- Boolean

let a: boolean = false;

console.log(a);
console.log(typeof a);

a = true;
console.log(a);

// 4- inference & annotation

let ann: string = "Teste";
//ann = 1

let inf = "Teste";

//inf = 1
