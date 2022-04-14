// 1) Arrays

let numbers: number[] = [1, 2, 3];

numbers.push(5);
// numbers.push('teste')

// 2) Outra sintaxe de Array

const nums: Array<number> = [1, 2, 3];

// 3) Utilizando o any

const arr1: any = [1, "Arroz", "Olá", 100];

// 4) Tipando parâmetros

const soma = (a: number, b: number) => {
  console.log(a + b);
};

// 5) return tipado

const greeting = (name: string): string => {
  return `Olá ${name}`;
};

// 6) função anônima

setTimeout(function () {
  const sallary: number = 1000;

  //console.log(parseFloat(sallary))
}, 2000);

// 7) tipando objetos

function passCoordinates(coord: { x: number; y: number }) {
  console.log("X coordinates: " + coord.x);
  console.log("Y coordinates: " + coord.y);
}

const objCoord = { x: "Oi", y: 84.2 };
const objCoord2 = { x: 329, y: 84.2 };

//passCoordinates(objCoord)
passCoordinates(objCoord2);

// 8) Propriedades Opcionais

const showNumbers = (a: number, b: number, c?: number) => {
  console.log("A: " + a);
  console.log("B: " + b);
  if (c) {
    console.log("C: " + c);
  }
};

showNumbers(1, 2, 3);
showNumbers(4, 5);

// 9) Validando argumentos opcionais

const advancedGreeting = (firstName: string, lastName?: string) => {
  if (lastName !== undefined) {
    return `Olá, ${firstName} ${lastName}, tudo bem ?`;
  }

  return `Olá, ${firstName}, tudo bem ?`;
};

console.log(advancedGreeting("Bola, Bolota"));
console.log(advancedGreeting("Juzinha"));

// 10) Validando argumentos opcionais

function showBalance(balance: string | number) {
  console.log(`O saldo da conta é R$${balance}`);
}

showBalance(500);
showBalance("100");

const arr2: Array<number | string | boolean> = [1, "Teste", true];

// 11) mais sobre union types

const showUserRole = (role: boolean | string) => {
  if (typeof role === "boolean") {
    console.log("Usuário não aprovado!");
  }
  console.log(`O usuário é um: ${role}`);
};

showUserRole(false);
showUserRole("Admin");
showUserRole("Editor");

// 12) Type alias

type ID = string | number;

function showId(id: ID) {
  console.log(`O ID é: ${id}`);
}

showId("1");
showId(20);

// 13) Interfaces

interface Point {
  x: number;
  y: number;
  z: number;
}

const showCoords = (obj: Point) => {
  console.log(`Y: ${obj.x} Y: ${obj.y} Z: ${obj.z}`);
};

const coordObj: Point = {
  x: 10,
  y: 15,
  z: 20,
};

showCoords(coordObj);

// 14) interface x type alias

interface Person {
  name: string;
}

interface Person {
  age: number;
}

const somePerson: Person = { name: "João", age: 25 };

type personType = {
  name: string;
};

//type personType = {
//    age: number
//}

// 15) literal types

let test: "testando";

test = "testando";

console.log(test);

const showDirection = (direction: "left" | "right" | "center") => {
  console.log(`A direção é: ${direction}`);
};

showDirection("left");
// showDirection("top")

// 16) non-null assertion

const p = document.getElementById("some-p");

console.log(p!.innerText);

// 17) big int

let n: bigint;

n = 1000n;
// console.log(n + 1)

console.log(n + 10n);

// 18) symbol

let symbolA = Symbol("a");
let symbolB = Symbol("a");

console.log(symbolA === symbolB);
