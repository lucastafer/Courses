///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times. Do this with a While Loop and a For Loop

// While Loop

var x = 0

while (x < 5) {
    console.log("Hello")
    x ++
}

// For Loop

for (z = 0; z < 5; z ++) {
    console.log("Bye")
}


/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25. Do this using two methods, a while loop and a for loop

// METHOD ONE
// While Loop

var y = 1

while(y < 25) {
    if (y % 2 !== 0) {
        console.log(`Odd number: ${y} `)
    }
    y ++
}

// METHOD TWO
// For Loop

for (w = 0; w < 25; w ++){
    if (w % 2 !== 0) {
        console.log(`Odd number: ${w}`)
    }
}