function addNewPhone() {
    const phoneForm = document.querySelector("form#phones") // querySelector é tipo o querySelectorAll, mas esse pega só o primeiro elemento.
    const newPhone = phoneForm.children[0].cloneNode(true) // o método children imprime todos os filhos que o phoneForm tem e o método cloneNode clona o elemento em questão. Recebe o parâmetro dip, que é true ou false. Se colocar false, ele só clona o P, se for true, clona o filhos, os filhos dos filhos, até o ultimo elemento.
    const phonePosition = phoneForm.children.length + 1
    newPhone.querySelector("label").innerText = "Telefone " + phonePosition + ": " //aqui estamos adicionando um texto ao elemento com o innerText.
    phoneForm.appendChild(newPhone) // Adiciona um nó ao final da lista de filhos de um nó pai especificado.
    console.log(phoneForm.children)
}

function printPhones() {
    let message = ""
    const phones = document.querySelectorAll("input[name='phone']")
    phones.forEach((phone, index) => {
        message += "Telefone " + (index + 1) + ": " + phone.value + "\n"
    })
    alert(message)
}