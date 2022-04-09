import { actionTypes } from "../constants/fruits";

const INITIAL_STATE = {
    fruits: [],
  };
  
  const reducers = (state = INITIAL_STATE, action) => {
    switch (action.type) {
      case actionTypes.ADD_FRUIT:
        return {fruits: [...state.fruits, {...action.payload}]}
      case actionTypes.REMOVE_FRUIT:
        return {fruits: state.fruits.filter((x) => x.id !== action.payload.id)}
      default:
        return state;
    }
  };
  
  export { reducers };
