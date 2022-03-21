class Spaceships {
    constructor(name, crewQuantity) {
        this.name = name
        this.crewQuantity = crewQuantity
        this.isHitched = false // Começam falso pois a nave só é engatada e tem as portas abertas após o cadastro dela.
        this.doorsOpen = false
    }

    hitch() { // Essa função aqui deve ser acionada ao efetuar o cadastro de uma nova nave lá quando selecionar a opção 1. Ela altera os status dos coiso pra True.
        this.isHitched = true
        this.doorsOpen = true
    }
}

function showMenu() {
    let chosenOption
    while(chosenOption != "1" && chosenOption != "2" && chosenOption != "3") {
        chosenOption = prompt(  "O que deseja fazer?\n" +
                                "1- Engatar nave\n" +
                                "2- Imprimir naves\n" +
                                "3- Sair do programa")
    }
    return chosenOption
}

function registerSpaceship() {
    let newSpaceship = prompt("Digite o nome da espaçonave.") // aqui primeiro definimos uma nova variavel local com os dados que queremos jogar depois pra classe.
    let crewQuantity = Number(prompt("Digite o número de tripulantes dessa espaçonave."))
    let spaceship = new Spaceships(newSpaceship, crewQuantity) //agora jogamos os dados prompt para a classe, com uma nova variável usando o método "new X" passando as variáveis como parâmetros.
    return spaceship
}

function printSpaceshipList(spaceships) {
    let spaceshipList = ""
    spaceships.forEach((spaceship, index) => {
        spaceshipList += (index + 1) + "- " + spaceship.name + " (" + spaceship.crewQuantity + " tripulantes)\n"
    })
    alert(spaceshipList)
}

let hitchedSpaceships = [] //criamos um array vazio para depois dar push com as infos
let chosenOption

while(chosenOption != "3") {
    chosenOption = showMenu()
    switch(chosenOption) {
        case "1":
            let spaceshipToAdd = registerSpaceship() // variável para efetivar o cadastro de uma nova nave com a função criada anteriormente.
            spaceshipToAdd.hitch() //aqui acionamos aquela função lá do começo, pois efetivando o cadastro, podemos engatar e abrir portas.
            hitchedSpaceships.push(spaceshipToAdd) //aqui adicionamos no array os dados dessa variável spaceshipToAdd
            break
        case "2":
            printSpaceshipList(hitchedSpaceships)
            break
    }
}