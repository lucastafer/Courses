import Spaceship from "./spaceship"
import SpaceshipEngine from "./spaceship_engine"


const sophia = new Spaceship("Sophia", 5, 10)
const amsterda = new Spaceship("Amsterdã", 10, 14)
const estrelaAna = new Spaceship("Estrela-Anã", 4, 20)

const sophiaEngine = new SpaceshipEngine(sophia)
const amsterdaEngine = new SpaceshipEngine(amsterda)
const estrelaAnaEngine = new SpaceshipEngine(estrelaAna)

sophiaEngine.turnOn()
amsterdaEngine.turnOn()
estrelaAnaEngine.turnOn()