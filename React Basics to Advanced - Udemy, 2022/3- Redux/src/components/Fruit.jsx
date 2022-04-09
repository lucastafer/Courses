import React from "react";
import { useDispatch } from "react-redux";
import {actions} from "../actions/Fruits.action"

export default function Fruit({ fruit }) {

  const dispatch = useDispatch();

  return (
    <div className="fruit">
      <ul>
        <li>
          <strong>Fruit: </strong> {fruit.name}
        </li>
        <li>
          <strong>Quantity: </strong> {fruit.quantity}
        </li>
      </ul>
      <button onClick={() => dispatch(actions.remove(fruit))}>Remove</button>
    </div>
  );
}
