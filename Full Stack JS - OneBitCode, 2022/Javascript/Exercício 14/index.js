let spaceship = {
    velocity: 0,
    speedUp: function(acceleration) {
        this.velocity += acceleration
    }
}

function registerSpaceship(){
    spaceship.name = prompt("Digite o nome da nave.")
    spaceship.type = prompt("Digite o tipo da nave.")
    spaceship.maxVelocity = Number(prompt("Digite a velocidade máxima permitida desta nave."))
}

function accelerate() {
    let acceleration = Number(prompt("Quanto você quer acelerar ?"))
    spaceship.speedUp(acceleration)
    if(spaceship.velocity > spaceship.maxVelocity) {
        alert(  "VELOCIDADE MÁXIMA ULTRAPASSADA!" +
                "\nVelocidade da Nave: " + spaceship.velocity + "km/s" + 
                "\nVelocidade máxima da Nave: " + spaceship.maxVelocity + "km/s")         
    }
}

function stop() {
    alert(  "Nome: " + spaceship.name + "\nTipo: " + spaceship.type + "\nVelocidade da nave: " 
            + spaceship.velocity + "\nMáxima da Nave: " + spaceship.maxVelocity)
    spaceship.velocity = 0
}

function menu() {
    let chosenOption
    do {
        chosenOption = prompt("Você deseja:\n1- Acelerar\n2-Parar")
        switch(chosenOption) {
            case "1":
                accelerate()
                break
            case "2":
                stop()
                break
            default:
                alert("Opção inválida.")
        }
    } while (chosenOption != "2")
}

registerSpaceship()
menu()