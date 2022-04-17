"use strict";
// 1) Arrays
let numbers = [1, 2, 3];
numbers.push(5);
// numbers.push('teste')
// 2) Outra sintaxe de Array
const nums = [1, 2, 3];
// 3) Utilizando o any
const arr1 = [1, "Arroz", "Olá", 100];
// 4) Tipando parâmetros
const soma = (a, b) => {
    console.log(a + b);
};
// 5) return tipado
const greeting = (name) => {
    return `Olá ${name}`;
};
// 6) função anônima
setTimeout(function () {
    const sallary = 1000;
    //console.log(parseFloat(sallary))
}, 2000);
// 7) tipando objetos
function passCoordinates(coord) {
    console.log("X coordinates: " + coord.x);
    console.log("Y coordinates: " + coord.y);
}
const objCoord = { x: "Oi", y: 84.2 };
const objCoord2 = { x: 329, y: 84.2 };
//passCoordinates(objCoord)
passCoordinates(objCoord2);
// 8) Propriedades Opcionais
const showNumbers = (a, b, c) => {
    console.log("A: " + a);
    console.log("B: " + b);
    if (c) {
        console.log("C: " + c);
    }
};
showNumbers(1, 2, 3);
showNumbers(4, 5);
// 9) Validando argumentos opcionais
const advancedGreeting = (firstName, lastName) => {
    if (lastName !== undefined) {
        return `Olá, ${firstName} ${lastName}, tudo bem ?`;
    }
    return `Olá, ${firstName}, tudo bem ?`;
};
console.log(advancedGreeting("Bola, Bolota"));
console.log(advancedGreeting("Juzinha"));
// 10) Validando argumentos opcionais
function showBalance(balance) {
    console.log(`O saldo da conta é R$${balance}`);
}
showBalance(500);
showBalance("100");
const arr2 = [1, "Teste", true];
// 11) mais sobre union types
const showUserRole = (role) => {
    if (typeof role === "boolean") {
        console.log("Usuário não aprovado!");
    }
    console.log(`O usuário é um: ${role}`);
};
showUserRole(false);
showUserRole("Admin");
showUserRole("Editor");
function showId(id) {
    console.log(`O ID é: ${id}`);
}
showId("1");
showId(20);
const showCoords = (obj) => {
    console.log(`Y: ${obj.x} Y: ${obj.y} Z: ${obj.z}`);
};
const coordObj = {
    x: 10,
    y: 15,
    z: 20,
};
showCoords(coordObj);
const somePerson = { name: "João", age: 25 };
//type personType = {
//    age: number
//}
// 15) literal types
let test;
test = "testando";
console.log(test);
const showDirection = (direction) => {
    console.log(`A direção é: ${direction}`);
};
showDirection("left");
// showDirection("top")
// 16) non-null assertion
const p = document.getElementById("some-p");
console.log(p.innerText);
// 17) big int
let n;
n = 1000n;
// console.log(n + 1)
console.log(n + 10n);
// 18) symbol
let symbolA = Symbol("a");
let symbolB = Symbol("a");
console.log(symbolA === symbolB);
