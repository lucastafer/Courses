// 1) Interface as argument

interface Product {
  name: string;
  price: number;
  isAvailable: true;
}

function showProductDetails(product: Product) {
  console.log(
    `The product name is ${product.name} and it costs ${product.price}`
  );
  if (product.isAvailable) {
    console.log("This product is available.");
  }
}

const shirt: Product = {
  name: "T-Shirt",
  price: 19.9,
  isAvailable: true,
};

showProductDetails(shirt);

// 2) Optional property on Interfaces

interface User {
  email: string;
  role?: string;
}

function showUserDetails(user: User) {
  console.log(`User e-mail: ${user.email}`);
  if (user.role) {
    console.log(`User role: ${user.role}`);
  }
}

const u1: User = { email: "lucas@lucas.com", role: "Admin" };

const u2: User = { email: "bolinha@bol.com" };

showUserDetails(u1);
showUserDetails(u2);

// 3) readonly

interface Car {
  brand: string;
  readonly wheels: number;
}

const fusca: Car = {
  brand: "VW",
  wheels: 4, //value definition, now it can't be changed in the future.
};

//fusca.wheels = 5

// 4) index signature

interface CoordObject {
  [index: string]: number;
}

let coords: CoordObject = {
  x: 10,
};

coords.y = 15;
//coords.z = "teste"

// 5) Extending types

interface Human {
  name: string;
  age: number;
}

interface SuperHuman extends Human {
  superpowers: string[];
}

const lucas: Human = {
  name: "Lucas",
  age: 21,
};

const luffy: SuperHuman = {
  name: "Luffy",
  age: 21,
  superpowers: ["Gomu Gomu no Mi", "Haki"],
};

console.log(lucas);
console.log(luffy);
console.log(luffy.superpowers[1]);

// 6) intersection types

interface Character {
  name: string;
}

interface Gun {
  type: string;
  caliber: number;
}

type HumanWithGun = Character & Gun;

const usopp: HumanWithGun = {
  name: "Usopp",
  type: "Kabuto",
  caliber: 500,
};

console.log(usopp);
console.log(usopp.type);

// 7) readonly array

let myArray: ReadonlyArray<string> = ["Apple", "Orange", "Banana"];

myArray.forEach((item) => {
  console.log(`Fruit: ${item}`);
});

myArray = myArray.map((item) => {
  return `Fruit: ${item}`;
});

console.log(myArray);

// 8) tuples

type fiveNumbers = [number, number, number, number, number];

const myNumberArray: fiveNumbers = [1, 2, 3, 4, 5];
// const myArray2: fiveNumbers = [1, 2, 3, 4, 5, 6];
// const myArray3: fiveNumbers = [1, 2, 3, 4, "Test"];

type nameAndAge = [string, number];

const anotherUser: nameAndAge = ["Lucas", 21];

// 9) readonly tuples (like python)

function showNumbers(numbers: readonly [number, number]) {
  console.log(numbers[0]);
  console.log(numbers[1]);
  //numbers[0] = 10
}

showNumbers([1, 2]);
