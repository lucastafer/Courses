class Spaceship {
    constructor(name, crewQuantity) {
      this.name = name
      this.crewQuantity = crewQuantity
      this.currentVelocity = 0
    }
    speedUp(acceleration) {
      this.currentVelocity += (acceleration * 0.83)
    }
}