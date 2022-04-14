// 1) Importing files

import importGreet from "./greet.js";

importGreet();

// 2) Importing variables

import { x } from "./variable";

console.log(x);

// 3) Multiple imports

import { a, b, myFunction } from "./multiple";

console.log(a);
console.log(b);
myFunction();

// 4) Alias for import

import { someName as name } from "./changeName.js";

console.log(name);

// 5) Import all (*)

import * as myNumbers from "./numbers";

console.log(myNumbers);

const nx = myNumbers.n1;
console.log(nx);

//6) Importing types

import { Human } from "./mytypes.js";

function userDetails(user: Human) {
  return `Username: ${user.name}\nUser age: ${user.age}`;
}

const user: Human = {
  name: "Lucas",
  age: 21,
};

console.log(userDetails(user));
