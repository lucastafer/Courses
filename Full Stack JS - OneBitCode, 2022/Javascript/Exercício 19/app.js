class App {
    addProperty() {
        event.preventDefault()
        let buildingType = document.querySelector("select[name='buildingType']").value
        let buildingArea = document.querySelector("input[name='buildingArea']").value
        let rented = document.querySelector("input[name='rented']").checked
        let property = new Property(buildingType, buildingArea, rented)
        this.addOnPropertiesList(property)
        this.cleanForm()
    }
    
    addOnPropertiesList(property) {
        let listElement = document.createElement("li")
        let propertyInfo = `Tipo: ${property.buildingType} (Área: ${property.buildingArea} m²)`
        if(property.rented) {
            let rentedMark = this.createRentedMark()
            listElement.appendChild(rentedMark)
        }
        listElement.innerHTML += propertyInfo
        let buttonToRemove = this.createRemoveButton()
        listElement.appendChild(buttonToRemove)
        document.getElementById("properties").appendChild(listElement)
    }

    createRentedMark() {
        let rentedMark = document.createElement("span")
        rentedMark.style.color = "white"
        rentedMark.style.background = "red"
        rentedMark.innerText = "ALUGADO"
        return rentedMark
    }

    createRemoveButton() {
        let buttonToRemove = document.createElement("button")
        buttonToRemove.setAttribute("onclick", "app.remove()")
        buttonToRemove.innerText = "Remover"
        return buttonToRemove
    }

    cleanForm() {
        document.querySelector("input[name='area']").value = ""
        document.querySelector("input[name='rented'").checked = false
    }

    remove() {
        let liToRemove = event.target.parentNode
        document.getElementById("properties").removeChild(liToRemove)
    }
}