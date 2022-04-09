// Função para acessar os inputs
function showInfo() {
    let name = document.querySelector("input[name='name']").value //pega a resposta do input name com name 'name'
    let favoriteColor = document.querySelector("select[name='color'] option:checked").text //pega os dados do select de name 'color', tem que por esse checked
    let likeProgramming = document.querySelector("input[name='like-programming']:checked").value //pega a opção escolhida no input de name 'like-programming', tem que por esse checked
    let developerOptions = document. querySelectorAll("input[name=developer-options]:checked") //como é um checkbox e podemos ter mais de uma resposta, usa o qsAll para pegar todas.
    let optionsValue = [] //array para selecionar todos os os valores marcados na checkbox developerOptions acima.
    developerOptions.forEach(element => { optionsValue.push(element.value) })
    let optionsChecked = optionsValue.join(", ")
    alert(`Nome: ${name}\nCor primária: ${favoriteColor}\nGosta de programar ? ${likeProgramming}\nConhecimentos em programação web: ${optionsChecked}`)
}