let pilotName = prompt("Bem-vindo (a)! Qual seu nome, piloto(a) ?")
let velocity = 0

let chooseVelocity = prompt("Qual a velocidade desejada " + pilotName + " ?")

let velocityConfirmation = confirm("Por favor confirme a velocidade desejada.\nConfirmar ajuste da velocidade para " + chooseVelocity + " Km/h ?")
if(velocityConfirmation) {
    alert("Velocidade ajustada para " + chooseVelocity + " Km/h...")
    velocity = chooseVelocity
    if(velocity <= 0) {
        alert("Nave está parada. Considere partir e, para isso, aumentar a velocidade.")
    } else if(velocity < 40) {
        alert("Você está devagar, podemos acelerar mais.")
    } else if(velocity < 80) {
        alert("Parece uma boa velocidade, mantenha assim.")
    } else if(velocity < 100) {
        alert("Velocidade alta, considere diminuir.")
    } else{
        alert("Velocidade perigosa. Controle automático forçado.")
    }
}else {
    alert("Ajuste de velocidade cancelado. Velocidade permanece zerada.")
}

alert("Piloto(a) " + pilotName + " está atualmente a " + velocity + " Km/h.")