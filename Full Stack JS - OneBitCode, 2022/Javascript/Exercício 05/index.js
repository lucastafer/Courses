let lyDistance = prompt("Digite uma distância em Anos-Luz.")

let chooseOption = prompt("Vamos transformar essa distância em alguma das unidades de medida abaixo. Escolha qual deseja:\n1- Parsec (pc)\n2- Unidade Astronônima (AU)\n3- Quilômetro (Km)")

switch(chooseOption) {
    case "1":
        let pcOption = lyDistance * 0.306601
        alert("Convertendo" + chooseOption + " Anos-Luz em Parsec, temos " + pcOption + " pc.")
        break
    case "2":
        let auOption = lyDistance * 63241.1
        alert("Convertendo" + chooseOption + " Anos-Luz em Unidade Astronônima, temos " + auOption + " AU.")
        break
    case "3":
        let kmOption = lyDistance * (9.5 * (10**12))
        alert("Convertendo" + chooseOption + " Anos-Luz em Quilômetros, temos " + kmOption + " Km.")
        break
    default:
        alert("Opção inválida.")
}