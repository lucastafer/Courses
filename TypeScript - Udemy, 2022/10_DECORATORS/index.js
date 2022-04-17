"use strict";
// 1) First decorator
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
function myDecorator() {
    console.log("Initializing decorator!");
    return function (target, propertKey, descriptor) {
        console.log("Executing decorator!");
        console.log(target);
        console.log(propertKey);
        console.log(descriptor);
    };
}
class myClass {
    testing() {
        console.log("Finishing method execution.");
    }
}
__decorate([
    myDecorator()
], myClass.prototype, "testing", null);
const myObj = new myClass();
myObj.testing();
// 2) Multiple decorators
function a() {
    return function (target, propertKey, descriptor) {
        console.log("A executed.");
    };
}
function b() {
    return function (target, propertKey, descriptor) {
        console.log("B executed.");
    };
}
class MultipleDecorators {
    testing() {
        console.log("Execution done.");
    }
}
__decorate([
    a(),
    b()
], MultipleDecorators.prototype, "testing", null);
// 3) Class decorator
function classDecorator(constructor) {
    console.log(constructor.name);
    if (constructor.name === "User") {
        console.log("Registering user...");
    }
}
let User = class User {
    constructor(name) {
        this.name = name;
    }
};
User = __decorate([
    classDecorator
], User);
const lucas = new User("Lucas");
console.log(lucas);
//4) Method decorator
function enumerable(value) {
    return function (target, propertKey, descriptor) {
        descriptor.enumerable = value;
    };
}
class Machine {
    constructor(name) {
        this.name = name;
    }
    showName() {
        console.log(this);
        return `Machine name is: ${this.name}`;
    }
}
__decorate([
    enumerable(false)
], Machine.prototype, "showName", null);
const truck = new Machine("Truck");
// 5) Acessor decorator
class Pokemon {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    get showName() {
        return `Pokémon's name: ${this.name}`;
    }
    get showAge() {
        return `Pokémon's age: ${this.age}`;
    }
}
__decorate([
    enumerable(true)
], Pokemon.prototype, "showName", null);
__decorate([
    enumerable(false)
], Pokemon.prototype, "showAge", null);
const gengar = new Pokemon("Gengar", 10);
console.log(gengar);
// 6) Property decorator
function formatNumber() {
    return function (target, propertyKey) {
        let value;
        const getter = function () {
            return value;
        };
        const setter = function (newVal) {
            value = newVal.padStart(5, "0");
        };
        Object.defineProperty(target, propertyKey, {
            set: setter,
            get: getter,
        });
    };
}
class ID {
    constructor(id) {
        this.id = id;
    }
}
__decorate([
    formatNumber()
], ID.prototype, "id", void 0);
const newItem = new ID("1");
console.log(newItem);
// 7) Real application: Class decorator
function createdDate(created) {
    created.prototype.createdAt = new Date();
}
let Book = class Book {
    constructor(id) {
        this.id = id;
    }
};
Book = __decorate([
    createdDate
], Book);
let Pen = class Pen {
    constructor(id) {
        this.id = id;
    }
};
Pen = __decorate([
    createdDate
], Pen);
const newBook = new Book(12);
const newPen = new Pen(10);
// 8) Real application: Method decorator
function checkIfUserPosted() {
    return function (target, key, descriptor) {
        const childFunction = descriptor.value;
        console.log(childFunction);
        descriptor.value = function (...args) {
            if (args[1] === true) {
                console.log("User already posted!");
                return null;
            }
            else {
                return childFunction.apply(this, args);
            }
        };
        return descriptor;
    };
}
class Post {
    constructor() {
        this.alreadyPosted = false;
    }
    post(content, alreadyPosted) {
        this.alreadyPosted = true;
        console.log(`User post: ${content}`);
    }
}
__decorate([
    checkIfUserPosted()
], Post.prototype, "post", null);
const newPost = new Post();
newPost.post("My first post!", newPost.alreadyPosted);
// 9) Real application: Property decorator
function Max(limit) {
    return function (target, propertyKey) {
        let value;
        const getter = function () {
            return value;
        };
        const setter = function (newVal) {
            if (newVal.length > limit) {
                console.log(`Value must have maximum ${limit} digits`);
                return;
            }
            else {
                value = newVal;
            }
            Object.defineProperty(target, propertyKey, {
                get: getter,
                set: setter,
            });
        };
    };
}
class Admin {
    constructor(username) {
        this.username = username;
    }
}
__decorate([
    Max(10)
], Admin.prototype, "username", void 0);
