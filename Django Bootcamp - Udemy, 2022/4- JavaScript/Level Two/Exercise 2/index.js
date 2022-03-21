// Main array
var roster = []

// Add New Student function
function addNew() {
    var newName = prompt("What name would you like to add ?")
    roster.push(newName)
}

// Remove Student Function
function remove() {
    var removeName = prompt("What name would you like to remove ?")
    if(roster.indexOf(removeName) > -1) {
        roster = roster.filter(name => name !== removeName) // Filter cria um novo array sem esse que especificamos
        console.log(`${removeName} removed successfully.`)
    } else {
        console.log(`You haven't registered the name ${removeName} yet.\nPlease try another name or register this.`)
    }
}

/* 
We can do the remove function like this too:

function remove() {
    var removeName = prompt("What name would you like to remove ?")
    var index = roster.indexOf(removeName) Firstly we localize the index of removeName.
    roster.splice(index, 1) Later we cut him with the splice method. The number is how many qe want to cut (to situations with more than 2 names equals).
}
*/

// Display Function
function display() {
    console.log(roster)
}

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.

var start = prompt("Would you like to start the roster web app? y/n")
var request = "empty"

if(start == "y") {
    while (request !== "quit") {
        request = prompt("Please select an action: add, remove, display, or quit.")
        if(request == "add") {
            addNew()
        }else if(request == "remove") {
            remove()
        }else if(request == "display") {
            display()
        }
    }
}

alert("Thanks for using the Web App! Please refresh the page to start over.")
