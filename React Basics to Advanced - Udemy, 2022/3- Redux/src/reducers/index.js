import { combineReducers } from "redux";
import {reducers as fruitReducers} from "./Fruit.reducer"

const reducers = combineReducers({
    fruitReducers
})

export {reducers};
