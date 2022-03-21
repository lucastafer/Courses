/* 

1. Considere o seguinte Array:

let spaceshipNames = ["Golias", "Elemental", "Helmet"]

Se quisermos adicionar "Colossus", de forma que ele fique na última posição, que método devo usar ?

R: spaceshipNames.push("Colossus")

2. O que seria impresso no console como o seguinte código ?

let spaceships = [["Colossus", 40], ["Elemental", 20], "Golias", "Helmet"]
console.log(spaceships[2][1])

R: "o"

3. Qual será o valor de randomSpaceships abaixo?

let discoverySpaceships = ["Elemental", "Darwin", "Ártemis"]
let battleSpaceships = ["Fenix", "Golias", "Helmet"]
let extractionSpaceships = ["Deméter", "Puller"]

let randomSpaceships = [
 discoverySpaceships.indexOf("Elemental"), 
 battleSpaceships.indexOf("Helmet"), 
 extractionSpaceships.indexOf("Puller")
]

R: [0, 2, 1] 

4. Qual será o resultado o array spaceshipsList abaixo?

let spaceshipsList = ["Colossus", "Helmet", ["Fenix", "Revivor"], "Supernova"]
spaceshipsList.pop()
spaceshipsList.pop()
spaceshipsList.push("Elemental")
spaceshipsList.unshift("Eagle")
spaceshipsList.shift()
spaceshipsList.unshift("")

R: ["", "Colossus", "Helmet", "Elemental"]

*/
