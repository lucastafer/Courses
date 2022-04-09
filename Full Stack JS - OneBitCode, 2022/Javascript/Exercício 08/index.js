let spaceshipName = prompt("Olá, astronauta!\nPor favor, insira o nome de sua astronave.")
let newSpaceshipName = ""

for(let pos = spaceshipName.length - 1; pos >= 0; pos -= 1) {
    if(spaceshipName[pos] == "e") {
        break
    } else{
        newSpaceshipName += spaceshipName[pos]
    }
}

alert("Nome original da nave: " + spaceshipName + "\nNome após ocultação: " + newSpaceshipName)