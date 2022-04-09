let spaceshipName = prompt("Olá, Viajante!\nDigite o nome da sua aeronave.")
let cont = 0

while(true) {
    let dobraOption = prompt("Deseja entrar em dobra espacial ?\n1- Sim\n2- Não")
        if(dobraOption == "1") {
            alert("Dobra realizada com sucesso!")
            cont += 1
        } else if(dobraOption == "2") {
            alert("Dobra não realizada.\nAeronave " + spaceshipName + " pousando com " + cont + " dobras realizadas.")
            break
        } else{
            alert("Opção inválida.")
        }
}