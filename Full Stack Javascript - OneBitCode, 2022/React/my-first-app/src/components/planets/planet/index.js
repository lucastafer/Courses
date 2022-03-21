import React, { Fragment, useEffect, useState } from "react";
import GrayImg from "../../shared/gray-img";
import LinkDescription from "../../shared/description-link";
import { Link } from 'react-router-dom';


const Planet = (props) => {

    let title
    if(props.title_with_underline)
        title = <h4><u>{props.name}</u></h4>
    else
        title = <h4>{props.name}</h4>
    
    

    return (
        <div>
            <Link to={`/planet/${props.id}`}>{title}</Link>
            <LinkDescription description={props.description} link={props.link}></LinkDescription>
            <GrayImg img_url={props.img_url} gray={props.gray}/>
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
