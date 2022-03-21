let spaceshipName = prompt("Olá, astronauta!\nPor favor, insira o nome de sua espaçonave.")
let oldCharacter = prompt("Insira agora o caractere que deseja substituir.")
let newCharacter = prompt("Insira agora o caractere por qual deseja substituir.")
let newSpaceship = ""

for(let pos = 0; pos < spaceshipName.length; pos += 1) {
    if(spaceshipName[pos] == oldCharacter){
        newSpaceship += newCharacter
    } else {
        newSpaceship += spaceshipName[pos]
    }
}

alert("O novo nome da aeronave é " + newSpaceship)