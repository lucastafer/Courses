const hitchedSpaceships = [
    ["Fenix", 8, true],
    ["Golias", 10, true],
    ["Helmet", 5, false],
    ["Elemental", 3, true],
    ["Darwin", 15, false]
    ]

let crewGreaterThan9 = hitchedSpaceships.filter(spaceship => {
    return spaceship[1] > 9
}).map (spaceship => {
    return spaceship[0]
})

let pendingHitch = hitchedSpaceships.findIndex(spaceship => {
    return spaceship[2] == false
})

let upcasedSpaceships = hitchedSpaceships.map(spaceship => {
    return spaceship[0].toUpperCase()
})


alert(
    "Naves com mais de 9 tripulantes: " + crewGreaterThan9.join(", ") +
    "\nPlataforma em processo de engate mais próxima: " + (pendingHitch + 1) +
    "\nTodas as aeronaves em ordem: " + upcasedSpaceships.join(", ")
)