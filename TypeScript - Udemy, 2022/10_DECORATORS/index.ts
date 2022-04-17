// 1) First decorator

function myDecorator() {
  console.log("Initializing decorator!");

  return function (
    target: any,
    propertKey: string,
    descriptor: PropertyDescriptor
  ) {
    console.log("Executing decorator!");
    console.log(target);
    console.log(propertKey);
    console.log(descriptor);
  };
}

class myClass {
  @myDecorator()
  testing() {
    console.log("Finishing method execution.");
  }
}

const myObj = new myClass();

myObj.testing();

// 2) Multiple decorators

function a() {
  return function (
    target: any,
    propertKey: string,
    descriptor: PropertyDescriptor
  ) {
    console.log("A executed.");
  };
}

function b() {
  return function (
    target: any,
    propertKey: string,
    descriptor: PropertyDescriptor
  ) {
    console.log("B executed.");
  };
}

class MultipleDecorators {
  @a()
  @b()
  testing() {
    console.log("Execution done.");
  }
}

// 3) Class decorator

function classDecorator(constructor: Function) {
  console.log(constructor.name);
  if (constructor.name === "User") {
    console.log("Registering user...");
  }
}

@classDecorator
class User {
  name;

  constructor(name: string) {
    this.name = name;
  }
}

const lucas = new User("Lucas");
console.log(lucas);

//4) Method decorator

function enumerable(value: boolean) {
  return function (
    target: any,
    propertKey: string,
    descriptor: PropertyDescriptor
  ) {
    descriptor.enumerable = value;
  };
}

class Machine {
  name;

  constructor(name: string) {
    this.name = name;
  }

  @enumerable(false)
  showName() {
    console.log(this);
    return `Machine name is: ${this.name}`;
  }
}

const truck = new Machine("Truck");

// 5) Acessor decorator

class Pokemon {
  name?;
  age?;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }
  @enumerable(true)
  get showName() {
    return `Pokémon's name: ${this.name}`;
  }
  @enumerable(false)
  get showAge() {
    return `Pokémon's age: ${this.age}`;
  }
}

const gengar = new Pokemon("Gengar", 10);

console.log(gengar);

// 6) Property decorator

function formatNumber() {
  return function (target: Object, propertyKey: string) {
    let value: string;

    const getter = function () {
      return value;
    };

    const setter = function (newVal: string) {
      value = newVal.padStart(5, "0");
    };

    Object.defineProperty(target, propertyKey, {
      set: setter,
      get: getter,
    });
  };
}

class ID {
  @formatNumber()
  id;

  constructor(id: string) {
    this.id = id;
  }
}

const newItem = new ID("1");
console.log(newItem);

// 7) Real application: Class decorator

function createdDate(created: Function) {
  created.prototype.createdAt = new Date();
}

@createdDate
class Book {
  id;
  createdAt?: Date;

  constructor(id: number) {
    this.id = id;
  }
}

@createdDate
class Pen {
  id;
  createdAt?: Date;

  constructor(id: number) {
    this.id = id;
  }
}

const newBook = new Book(12);
const newPen = new Pen(10);

// 8) Real application: Method decorator

function checkIfUserPosted() {
  return function (
    target: Object,
    key: string | Symbol,
    descriptor: PropertyDescriptor
  ) {
    const childFunction = descriptor.value;
    console.log(childFunction);
    descriptor.value = function (...args: any[]) {
      if (args[1] === true) {
        console.log("User already posted!");
        return null;
      } else {
        return childFunction.apply(this, args);
      }
    };
    return descriptor;
  };
}

class Post {
  alreadyPosted = false;

  @checkIfUserPosted()
  post(content: string, alreadyPosted: boolean) {
    this.alreadyPosted = true;
    console.log(`User post: ${content}`);
  }
}

const newPost = new Post();
newPost.post("My first post!", newPost.alreadyPosted);

// 9) Real application: Property decorator

function Max(limit: number) {
  return function (target: Object, propertyKey: string) {
    let value: string;

    const getter = function () {
      return value;
    };

    const setter = function (newVal: string) {
      if (newVal.length > limit) {
        console.log(`Value must have maximum ${limit} digits`);
        return;
      } else {
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
  @Max(10)
  username;

  constructor(username: string) {
    this.username = username;
  }
}
