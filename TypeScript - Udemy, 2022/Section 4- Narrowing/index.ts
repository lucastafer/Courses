// 1) type guard

const sum = (a: number | string, b: number | string) => {
  if (typeof a === "string" && typeof b === "string") {
    console.log(parseFloat(a) + parseFloat(b));
  } else if (typeof a === "number" && typeof b === "number") {
    console.log(a + b);
  } else {
    console.log("Impossible to sum.");
  }
};

sum("4", "9");
sum(12, 24);
sum("5", 6);

// 2) checking if a value exists

function operations(arr: number[], operation: string | undefined) {
  if (operation) {
    if (operation === "sum") {
      const sum = arr.reduce((i, total) => i + total);
      console.log(sum);
    } else if (operation === "multiply") {
      const multiply = arr.reduce((i, total) => i * total);
      console.log(multiply);
    }
  } else {
    console.log("Please choose an operation.");
  }
}

operations([10, 20, 30], "sum");
operations([10, 20, 30], "multiply");
operations([10, 20, 30], "");

// 3) instanceof

class User {
  name;
  constructor(name: string) {
    this.name = name;
  }
}

class SuperUser extends User {
  constructor(name: string) {
    super(name);
  }
}

const john = new User("John");
const paul = new SuperUser("Paul");

function userGreeting(user: object) {
  if (user instanceof SuperUser) {
    console.log(`Hello ${user.name}, want you to see system data ?`);
  } else if (user instanceof User) {
    console.log(`Hi, ${user.name}.`);
  }
}
userGreeting(john);
userGreeting(paul);

// 4) in operator

class Dog {
  name;
  breed;
  constructor(name: string, breed?: string) {
    this.name = name;
    if (breed) {
      this.breed = breed;
    }
  }
}

const carlinhos = new Dog("Carlinhos");
const bolinha = new Dog("Bolinha", "Yorkshire");


function showDogDetails(dog: Dog) {
  if('breed' in Dog) {
    console.log(`The dog's name is ${dog.name} and it's a ${dog.breed}.`)
  } else{
    console.log(`The dog's name is ${dog.name} and it's a street dog.`)
  }
}

console.log(carlinhos)
console.log(bolinha)