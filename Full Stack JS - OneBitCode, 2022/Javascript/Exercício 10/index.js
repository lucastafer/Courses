function slowDown(velocity, printer) {
    alert("Iniciando desaceleração para pouso e desembarque. Por favor aguardem.")
    while(true) {
        let newVelocity = velocity - 20
        velocity = newVelocity
        printer(newVelocity)
        if (newVelocity <= "0") {
            break
        }
    } 
    return newVelocity
}

let printVelocity = velocity => {
    if(velocity > "0"){
        alert("Desacelerando...\nVelocidade atual: " + velocity + " Km/s.")
    }else if(velocity < "0") {
        alert("Velocidade chegou a 0 Km/s. Comportas abertas e desembarque autorizado.")
    }
}

let newVelocity = slowDown(150, printVelocity)
    alert(newVelocity)