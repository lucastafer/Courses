const spaceship = {
    name: "Rontaro",
    currentBateryCharge: 100,      //carga atual da bateria
    consumptionPerKms: 0.00008    // consumo da bateria por segundo que ela fica em determinada velocidade
}

const updateBateryCharge = function(chargeConsumed) {      // primeira promise, que atualiza a carga da bateria com base na carga que foi consumida.
return new Promise((resolve, reject) => {      
    spaceship.currentBateryCharge -= chargeConsumed
    if(spaceship.currentBateryCharge > 0) {               // verifica se a carga é maior que 0. Se sim, resolve a promise com a carga atual da bateria.
    resolve(spaceship.currentBateryCharge)               // se for menor ou igual a zero, da o reject falando que a bateria foi esgotada.
    } else {
    reject("Bateria esgotada! Nave será desativada em alguns segundos.")
    }
})
}

const calculateBateryConsumption = function(velocity, seconds) {   // a segunda promise recebe a velocidade e por quantos segundos a nave ficou naquela velocidade.
    return new Promise((resolve, reject) => {                      // verifica se a velocidade e o consumo são igual ou menor que zero. Se for, está parada e dá reject.
        if(spaceship.consumptionPerKms <= 0 || velocity <= 0) {    // se não, ela calcula a carga consumida e dá resolve passando essa carga consumida como parâmetro.
        reject("Nave está parada!")
        } else {
        let chargeConsumed = spaceship.consumptionPerKms * velocity * seconds
        resolve(chargeConsumed) // o resultado dessa promise aqui será passado para a promise de cima.
    }
    })
}

calculateBateryConsumption(1, 5).then(chergConsumed => {       //definimos aqui por exemplo que a nave ficou a 90 km/s por 300 segundos.
    return updateBateryCharge(100)
}).then(newCharge => {
    console.log(`Carga atual: ${newCharge}`)
}).catch(error => {
    console.log(error)
})