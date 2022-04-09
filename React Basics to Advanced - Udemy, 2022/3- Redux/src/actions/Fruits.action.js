import { actionTypes } from '../constants/fruits';

const actions = {
    add: fruit => ({
        type: actionTypes.ADD_FRUIT,
        payload: fruit
    }),
    remove: fruit => ({
        type: actionTypes.REMOVE_FRUIT,
        payload: fruit
    }),
};

export {actions};
