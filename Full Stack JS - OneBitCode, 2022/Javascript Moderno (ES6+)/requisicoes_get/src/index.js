import "core-js"
import "regenerator-runtime"

import Neo from "./neo"
import { getNeos } from "./neo_services"

async function loadNeos () {
    let neos = []
    let neosJSON = await getNeos()
    neosJSON.forEach(neo => {
        const minDiameter = neo["estimated_diameter"]["kilometers"]["estimate_diameter_min"]
        const maxDiameter = neo["estimated_diameter"]["kilometers"]["estimate_diameter_max"]
        const averageDiameter = (minDiameter + maxDiameter) / 2
        const newNeo = new Neo(neo["id"], neo["name"], averageDiameter, neo["is_sentry_object"])
        neos.push(newNeo)
    })
    console.log(neos)
}