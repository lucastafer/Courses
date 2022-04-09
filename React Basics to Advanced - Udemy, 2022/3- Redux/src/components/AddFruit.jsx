import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { actions } from "../actions/Fruits.action"

export default function AddFruit() {
  const [name, setName] = useState("");
  const [quantity, setQuantity] = useState(0);

  const dispatch = useDispatch();

  const addFruit = (event) => {
    event.preventDefault();

    const fruit = {
      id: new Date(),
      name,
      quantity,
    };
    dispatch(actions.add(fruit));
  };

  return (
    <form onSubmit={addFruit}>
      <input
        type="text"
        name={name}
        placeholder="Fruit"
        required
        onChange={(event) => setName(event.target.value)}
      />
      <input
        type="number"
        name={quantity}
        placeholder="Quantity"
        required
        onChange={(event) => setQuantity(event.target.value)}
      />
      <button type="submit">Add</button>
    </form>
  );
}
