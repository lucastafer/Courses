// 1) Arrays
var numbers = [1, 2, 3];
numbers.push(5);
// numbers.push('teste')
// 2) Outra sintaxe de Array
var nums = [1, 2, 3];
// 3) Utilizando o any
var arr1 = [1, "Arroz", "Olá", 100];
// 4) Tipando parâmetros
var soma = function (a, b) {
    console.log(a + b);
};
// 5) return tipado
var greeting = function (name) {
    return "Ol\u00E1 ".concat(name);
};
// 6) função anônima
setTimeout(function () {
    var sallary = 1000;
    //console.log(parseFloat(sallary))
}, 2000);
// 7) tipando objetos
function passCoordinates(coord) {
    console.log("X coordinates: " + coord.x);
    console.log("Y coordinates: " + coord.y);
}
var objCoord = { x: "Oi", y: 84.2 };
var objCoord2 = { x: 329, y: 84.2 };
//passCoordinates(objCoord)
passCoordinates(objCoord2);
// 8) Propriedades Opcionais
var showNumbers = function (a, b, c) {
    console.log("A: " + a);
    console.log("B: " + b);
    if (c) {
        console.log("C: " + c);
    }
};
showNumbers(1, 2, 3);
showNumbers(4, 5);
// 9) Validando argumentos opcionais
var advancedGreeting = function (firstName, lastName) {
    if (lastName !== undefined) {
        return "Ol\u00E1, ".concat(firstName, " ").concat(lastName, ", tudo bem ?");
    }
    return "Ol\u00E1, ".concat(firstName, ", tudo bem ?");
};
console.log(advancedGreeting("Bola, Bolota"));
console.log(advancedGreeting("Juzinha"));
// 10) Validando argumentos opcionais
function showBalance(balance) {
    console.log("O saldo da conta \u00E9 R$".concat(balance));
}
showBalance(500);
showBalance("100");
var arr2 = [1, "Teste", true];
// 11) mais sobre union types
var showUserRole = function (role) {
    if (typeof role === "boolean") {
        console.log("Usuário não aprovado!");
    }
    console.log("O usu\u00E1rio \u00E9 um: ".concat(role));
};
showUserRole(false);
showUserRole("Admin");
showUserRole("Editor");
function showId(id) {
    console.log("O ID \u00E9: ".concat(id));
}
showId('1');
showId(20);
var showCoords = function (obj) {
    console.log("Y: ".concat(obj.x, " Y: ").concat(obj.y, " Z: ").concat(obj.z));
};
var coordObj = {
    x: 10,
    y: 15,
    z: 20
};
showCoords(coordObj);
var somePerson = { name: 'João', age: 25 };
//type personType = {
//    age: number
//}
// 15) literal types
var test;
test = "testando";
console.log(test);
var showDirection = function (direction) {
    console.log("A dire\u00E7\u00E3o \u00E9: ".concat(direction));
};
showDirection("left");
// showDirection("top")
// 16) non-null assertion
var p = document.getElementById('some-p');
console.log(p.innerText);
