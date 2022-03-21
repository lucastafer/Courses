// Prompts
var firstName = prompt("What is your first name ?")
var lastName =  prompt("What is your last name ?")
var age = prompt("How old are you ?")
var height = prompt("How tall are you (cm) ?")
var petName = prompt("What is the name of your pet ?")

// Conditions
var nameCond = null
var ageCond = null
var heightCond = null
var petCond = null


// Firt letter checker
if (firstName[0] === lastName[0]) {
    nameCond = true
} else {
    nameCond = false
}

// Age between 20 to 30 checker
if (age > 20 && age < 30) {
    ageCond = true
} else {
    ageCond = false
}

// Tall checker (at least 170 cm)
if (height >= 170) {
    heightCond = true
} else {
    heightCond = false
}

// Pet name end with "y"
if (petName[petName.length-1] === "y") {
    petCond = true;
  }else{
    petCond = false;
}

// Geral checklist

if (nameCond && ageCond && heightCond && petCond) {
    console.log("Welcome, brother! You've passed the test.")
} else {
    console.log("Nothing to see here, go out.")
}