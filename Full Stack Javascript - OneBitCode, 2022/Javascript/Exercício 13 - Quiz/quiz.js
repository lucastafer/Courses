/*

1. Com base no seguinte objeto

let spacialStation = {

  name: "AR12",

  "platform quantity": 10

}

Como seria possível acessar a propriedade "platform quantity"

R: spacialStation["platform quantity"]


2. Qual será o valor impresso no console do código abaixo

let spacialStation = { name: "The Boat", platformQuantity: 5 }

spacialStation.name = "The Reign"

console.log(spacialStation)

R: {name: "The Reign", platformQuantity: 5}


3. O que seria impresso no console com o seguinte código


let spaceship = { name: "Golias", type: "Batalha" }

spaceship.crewQuantity = 5

spaceship["isHitched"] = true

console.log(spaceship)

R: {name: "Golias", type: "Batalha", crewQuantity: 5, isHitched: true}


4. Qual será o valor de spaceship no código abaixo?

let spaceship = { name: "Puller", type: "Extração" }

spaceship.crewQuantity = 10

spaceship.isHitched = true

spaceship = { }

R: {}


5. Qual será o resultado do objeto spaceship abaixo?

let spaceship = { }

spaceship.name = "Ártemis"

spaceship.type = "Descoberta"

spaceship["crew quantity"] = 6

spaceship["isHitched"] = false

R: { name: "Ártemis", type: "Descoberta", crew quantity: 6, isHitched: false }

*/