// 1) Generics revision
function showData(arg) {
    return "Data is: ".concat(arg);
}
console.log(showData(5));
console.log(showData("Testing..."));
// 2) Constraints in Generics
function showProductName(obj) {
    return "Product name is: ".concat(obj.name);
}
var myObj = { name: "Door", color: "White" };
var otherProduct = { name: "Car", wheels: 4, engine: 1.4 };
var wrongProduct = { price: 19.99, category: "Clothes" };
console.log(showProductName(myObj));
console.log(showProductName(otherProduct));
var myCar = { name: "Fusca", wheels: 4, engine: 1.0, color: "Blue" };
var myPen = {
    name: "Pen",
    wheels: false,
    engine: false,
    color: "Black"
};
// 4) Type parameters
function getSomeKey(obj, key) {
    return "The key ".concat(key, " is on object and has the value ").concat(obj[key]);
}
var server = {
    ssd: "512GB",
    ram: "16GB"
};
console.log(getSomeKey(server, "ssd"));
function showCharName(obj, name) {
    return "".concat(obj[name]);
}
var myChar = {
    name: "Lucas",
    age: 21,
    hasDriveLicense: true
};
console.log(showCharName(myChar, "name"));
// 6) typeof type operator
var userName = "Lucas";
var userName2 = "Bolinha";
var newTruck = {
    km: 10000,
    kg: 5000,
    description: "Truck to less "
};
function showKm(km) {
    console.log("Vehicle Km's: ".concat(km));
}
showKm(newTruck.km);
var newCar = {
    km: 5000,
    kg: 1000
};
showKm(newCar.km);
var someVar = 5;
var testing = "some text";
// const testing2:CustomType = "some"
