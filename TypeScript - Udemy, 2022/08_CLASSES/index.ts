// 1) Generics revision

function showData<T>(arg: T): string {
  return `Data is: ${arg}`;
}

console.log(showData(5));
console.log(showData("Testing..."));

// 2) Constraints in Generics

function showProductName<T extends { name: string }>(obj: T) {
  return `Product name is: ${obj.name}`;
}

const myObj = { name: "Door", color: "White" };
const otherProduct = { name: "Car", wheels: 4, engine: 1.4 };
const wrongProduct = { price: 19.99, category: "Clothes" };

console.log(showProductName(myObj));
console.log(showProductName(otherProduct));
//console.log(showProductName(wrongProduct))

// 3) Interfaces with Generics

interface MyObject<T, U, Q> {
  name: string;
  wheels: T;
  engine: U;
  color: Q;
}

type Car = MyObject<number, number, string>;
type Pen = MyObject<boolean, boolean, string>;

const myCar: Car = { name: "Fusca", wheels: 4, engine: 1.0, color: "Blue" };
const myPen: Pen = {
  name: "Pen",
  wheels: false,
  engine: false,
  color: "Black",
};

// 4) Type parameters

function getSomeKey<T, K extends keyof T>(obj: T, key: K) {
  return `The key ${key} is on object and has the value ${obj[key]}`;
}

const server = {
  ssd: "512GB",
  ram: "16GB",
};

console.log(getSomeKey(server, "ssd"));
// console.log(getSomeKey(server, "GPU"));

// 5) keyof type operator

type Character = { name: string; age: number; hasDriveLicense: boolean };

type C = keyof Character;

function showCharName(obj: Character, name: C): string {
  return `${obj[name]}`;
}

const myChar: Character = {
  name: "Lucas",
  age: 21,
  hasDriveLicense: true,
};

console.log(showCharName(myChar, "name"));

// 6) typeof type operator

const userName: string = "Lucas";

const userName2: typeof userName = "Bolinha";

type x = typeof userName;

// 7) Indexed Access Types

type Truck = { km: number; kg: number; description: string };

type Km = Truck["km"];

const newTruck: Truck = {
  km: 10000,
  kg: 5000,
  description: "Truck to less ",
};

function showKm(km: Km) {
  console.log(`Vehicle Km's: ${km}`);
}

showKm(newTruck.km);

const newCar = {
  km: 5000,
  kg: 1000,
};

showKm(newCar.km);

// 8) Conditional Expressions Type

interface A {}

interface B extends A {}

type myType = B extends A ? number : string;

const someVar: myType = 5;
//const someVar2: myType = "Oi"


// 9) Template literals type

type testA = "text"

type CustomType = `some ${testA}`

const testing: CustomType = "some text"
// const testing2:CustomType = "some"
