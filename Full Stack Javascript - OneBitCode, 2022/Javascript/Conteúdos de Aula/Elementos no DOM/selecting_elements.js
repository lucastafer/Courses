function show() {
    let element = document.getElementById("name")
    console.log(element.value)
}

function show() {
    let elements = document.getElementsByName("phone")
    console.log(elements.value)
}

function show() {
    let elements = document.querySelectorAll("div#phones input[name='phone']")
    console.log(elements[0].value)
}