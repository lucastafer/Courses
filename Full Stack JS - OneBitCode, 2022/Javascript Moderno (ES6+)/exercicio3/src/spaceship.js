class Spaceship {
    constructor(name, currentCharge, capacity) {
        this.name = name
        this.currentCharge =  currentCharge
        this.capacity = capacity
    }

    battery() {
        return this.currentCharge * 100 / this.capacity
    }
}

export default Spaceship