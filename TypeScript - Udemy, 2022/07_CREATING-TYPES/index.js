"use strict";
// 1) Generics revision
function showData(arg) {
    return `Data is: ${arg}`;
}
console.log(showData(5));
console.log(showData("Testing..."));
// 2) Constraints in Generics
function showProductName(obj) {
    return `Product name is: ${obj.name}`;
}
const myObj = { name: "Door", color: "White" };
const otherProduct = { name: "Car", wheels: 4, engine: 1.4 };
const wrongProduct = { price: 19.99, category: "Clothes" };
console.log(showProductName(myObj));
console.log(showProductName(otherProduct));
const myCar = { name: "Fusca", wheels: 4, engine: 1.0, color: "Blue" };
const myPen = {
    name: "Pen",
    wheels: false,
    engine: false,
    color: "Black",
};
// 4) Type parameters
function getSomeKey(obj, key) {
    return `The key ${key} is on object and has the value ${obj[key]}`;
}
const server = {
    ssd: "512GB",
    ram: "16GB",
};
console.log(getSomeKey(server, "ssd"));
function showCharName(obj, name) {
    return `${obj[name]}`;
}
const myChar = {
    name: "Lucas",
    age: 21,
    hasDriveLicense: true,
};
console.log(showCharName(myChar, "name"));
// 6) typeof type operator
const userName = "Lucas";
const userName2 = "Bolinha";
const newTruck = {
    km: 10000,
    kg: 5000,
    description: "Truck to less ",
};
function showKm(km) {
    console.log(`Vehicle Km's: ${km}`);
}
showKm(newTruck.km);
const newCar = {
    km: 5000,
    kg: 1000,
};
showKm(newCar.km);
const someVar = 5;
const testing = "some text";
// const testing2:CustomType = "some"
