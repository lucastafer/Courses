import {React, Fragment, useState} from "react";

const initialState = {
    name: ''
}

const Form = (props) => {
    const[fields, setFields] = useState({
        name: ''
    })

    const handleSatellitesChange = (e) => setFields ({
        ...fields,
        [e.currentTarget.name]: e.currentTarget.value
    })

    const handleSubmit = (event) => {
        props.addSatellite(fields)
        event.preventDefault()
        setFields(initialState)
    }

    
    return(
        <Fragment>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="name">Satélite: </label>
                    <input id="name" type="text" name="name" value={fields.name} onChange={handleSatellitesChange}/>
                </div>
                <br></br>
                <input type="submit"></input>
            </form>
        </Fragment>
    )
}

export default Form
