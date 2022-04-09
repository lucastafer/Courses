function addHouse() {
    let number = document.querySelector("input[name='house-number']").value
    let district = document.querySelector("input[name='house-district']").value
    let city = document.querySelector("input[name='house-city']").value
    let area = document.querySelector("input[name='house-area']").value
    let newListValue = document.createElement("li")
    newListValue.innerText = area + "m², número " + number + " (" + district
    let removeButton = document.createElement("button")
    removeButton.type = "button"
    removeButton.innerText = "Remover"
    removeButton.setAttribute("onclick", "removeHouse(this)")
    newListValue.appendChild(removeButton)
    document.getElementById("house-list").appendChild(newListValue)
}

function removeHouse(button) {
    let liToRemove = button.parentNode
    document.getElementById("house-list").removeChild(liToRemove)
}