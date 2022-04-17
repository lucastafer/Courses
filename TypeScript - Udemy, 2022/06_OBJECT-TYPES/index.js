"use strict";
// 1) Interface as argument
function showProductDetails(product) {
    console.log(`The product name is ${product.name} and it costs ${product.price}`);
    if (product.isAvailable) {
        console.log("This product is available.");
    }
}
const shirt = {
    name: "T-Shirt",
    price: 19.9,
    isAvailable: true,
};
showProductDetails(shirt);
function showUserDetails(user) {
    console.log(`User e-mail: ${user.email}`);
    if (user.role) {
        console.log(`User role: ${user.role}`);
    }
}
const u1 = { email: "lucas@lucas.com", role: "Admin" };
const u2 = { email: "bolinha@bol.com" };
showUserDetails(u1);
showUserDetails(u2);
const fusca = {
    brand: "VW",
    wheels: 4, //value definition, now it can't be changed in the future.
};
let coords = {
    x: 10,
};
coords.y = 15;
const lucas = {
    name: "Lucas",
    age: 21,
};
const luffy = {
    name: "Luffy",
    age: 21,
    superpowers: ["Gomu Gomu no Mi", "Haki"],
};
console.log(lucas);
console.log(luffy);
console.log(luffy.superpowers[1]);
const usopp = {
    name: "Usopp",
    type: "Kabuto",
    caliber: 500,
};
console.log(usopp);
console.log(usopp.type);
// 7) readonly array
let myArray = ["Apple", "Orange", "Banana"];
myArray.forEach((item) => {
    console.log(`Fruit: ${item}`);
});
myArray = myArray.map((item) => {
    return `Fruit: ${item}`;
});
console.log(myArray);
const myNumberArray = [1, 2, 3, 4, 5];
const anotherUser = ["Lucas", 21];
// 9) readonly tuples (like python)
function showNumbers(numbers) {
    console.log(numbers[0]);
    console.log(numbers[1]);
    //numbers[0] = 10
}
showNumbers([1, 2]);
