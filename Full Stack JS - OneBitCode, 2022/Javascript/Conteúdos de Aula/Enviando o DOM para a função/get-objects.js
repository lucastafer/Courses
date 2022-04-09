function sayMyFirstName(element) {
    alert("Meu primeiro nome é "+ element.value)
}

function sayMyLastName() {
    console.log(event) // cada vez que um evento é chamado, ele é armazenado na variável event. Ele armazena sempre o último evento que foi chamado no DOM.
    alert("Meu último nome é " + event.target.value) // o event.target acessa o elemento que o chamou no html, no caso aquele input last-name. O value pega o valor que foi digitado.
}