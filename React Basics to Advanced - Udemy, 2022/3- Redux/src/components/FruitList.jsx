import React from "react";
import { useSelector } from "react-redux";
import AddFruit from "./AddFruit";
import Fruit from "./Fruit";

export default function FruitList() {
  const fruits = useSelector((state) => state.fruitReducers.fruits);

  return (
    <>
      <h1>Fruit List</h1>
      <AddFruit />
      {fruits.map((fruit) => (
        <Fruit key={fruit.id} fruit={fruit} />
      ))}
    </>
  );
}
