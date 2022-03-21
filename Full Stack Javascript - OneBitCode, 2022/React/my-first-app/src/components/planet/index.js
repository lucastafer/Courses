import React, { Fragment, useEffect, useState } from "react";
import GrayImg from "../shared/gray-img";
import LinkDescription from "../shared/description-link"
import Form from './form/form'
import { useParams, useNavigate, Navigate } from 'react-router-dom';


async function GetPlanet(id) {
    let response = await fetch(`http://localhost:3000/api/${id}.json`)
    let data = await response.json()
    return data
}

const Planet = () => {
    const[satellites, setSatellites] = useState([])
    const[planet, setPlanet] = useState({})
    const[redirect, setRedirect] = useState()

    let { id } = useParams()
    let navigate = useNavigate()

    useEffect(() => {
        GetPlanet(id).then(data => {
            setSatellites(data['satellites'])
            setPlanet(data['data'])
        }, error => {
            setRedirect(true)
        })
    }, [])

    const GoToPlanets = () => {
        navigate('/')
    }

    const addSatellite = (new_sattelite) => {
        setSatellites([...satellites, new_sattelite])
    }


    let title
    if(planet.title_with_underline)
        title = <h4><u>{planet.name}</u></h4>
    else
        title = <h4>{planet.name}</h4>
    
    if(redirect)
        return <Navigate to='/'/>

    return (
        <div>
            {title}
            <LinkDescription description={planet.description} link={planet.link}></LinkDescription>
            <GrayImg img_url={planet.img_url} gray={planet.gray}/>
            <h4>Satélites</h4>
            <Form addSatellite={addSatellite}/>
            <hr></hr>
                <ul>
                {satellites.map((satellite, index) =>
                    <li key={index}>{satellite.name}</li>
                )}
                </ul>
            <hr></hr>
            <button type="button" onClick={GoToPlanets}>Voltar à página inicial.</button>
        </div>
    )
}


/*
class Planet extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            satellites: [

            ]
        }
    }

    componentDidMount() {
        GetSatellites(this.props.id).then(data => {
            this.setState(state => ({
                satellites: data['satellites']
            }))
        })
    }

    render() {
        let title
        if(this.props.title_with_underline)
        title = <h4><u>{this.props.name}</u></h4>
        else
            title = <h4>{this.props.name}</h4>
    return (
        <div>
            {title}
            <LinkDescription description={this.props.description} link={this.props.link}></LinkDescription>
            <GrayImg img_url={this.props.img_url} gray={this.props.gray}/>
            <h4>Satélites</h4>
            {this.state.satellites.map((satellite, index) =>
                <ul>
                    <li key={index}>{satellite.name}</li>
                </ul>
            )}
            <hr></hr>
        </div>
    )
    }
}

const Planet = (props) => {
    const names = ['a', 'b', 'c', 'd']

    let title
    if(props.title_with_underline)
        title = <h4><u>{props.name}</u></h4>
    else
        title = <h4>{props.name}</h4>
    return (
        <div>
            {title}
            <LinkDescription description={props.description} link={props.link}></LinkDescription>
            <GrayImg img_url={props.img_url} gray={props.true}/>
            <hr></hr>
        </div>
    )
}
*/

export default Planet
