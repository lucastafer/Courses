import React, {Fragment, useState, useEffect} from "react";
import Planet from './planet';
import Form from '../planets/form'

async function GetPlanets(){
    let response = await fetch('http://localhost:3000/api/planets.json')
    let data = await response.json()
    return data
}

const Planets = () => {
    const [planets, setPlanets] = useState([
        {
            "id": "mars",
            "name": "Mars",
            "description": "Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System after Mercury. In English, Mars carries a name of the Roman god of war and is often referred to as the 'Red Planet'.",
            "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/OSIRIS_Mars_true_color.jpg/220px-OSIRIS_Mars_true_color.jpg",
            "link": "https://en.wikipedia.org/wiki/Mars"
          }
    ])

    useEffect(() => {
        GetPlanets().then(data => {
            setPlanets(data['planets'])
        })
    }, [])

    const addPlanet = (new_planet) => {
        setPlanets([...planets, new_planet])
    }

    return (
        <Fragment>
            <h3>Planet list</h3>
            <hr></hr>
            <Form addPlanet={addPlanet}/>
            <hr></hr>
            <hr/>
            {planets.map((planet, index) =>
                <Planet 
                id={planet.id}
                name = {planet.name}
                description = {planet.description}
                img_url = {planet.img_url}
                link = {planet.link}
                key = {index}
                />
            )}
        </Fragment>
    )
}

export default Planets


//CLASS COMPONENT EXAMPLE (CLASSIC)

/* class Planets extends React.Component {
    constructor(props){
        super(props)
        this.state = {
            planets: [ ]
        }
    }
    

    componentDidMount() {
        GetPlanets().then(data => {
            this.setState(state => ({
                planets: data['planets']
            }))
        })
    }

    removeLast = () => {
        let new_planets = [...this.state.planets]
        new_planets.pop()
        this.setState(state => ({
            planets: new_planets
        }))
    }

    duplicateLastPlanet = () => {
        let last_planet = this.state.planets[this.state.planets.length - 1]
        this.setState(state => ({
            planets: [...this.state.planets, last_planet]
        }))
    }

    render() {
        return (
            <Fragment>
                <h3>Planet list</h3>
                <button onClick={this.removeLast}>Remove Last</button>
                <button onClick={this.duplicateLastPlanet}>Duplicate Last</button>
                <hr/>
                {this.state.planets.map((planet, index) =>
                    <Planet 
                    id={planet.id}
                    name = {planet.name}
                    description = {planet.description}
                    img_url = {planet.img_url}
                    link = {planet.link}
                    key = {index}
                    />
                )}
            </Fragment>
        )
    }
} */