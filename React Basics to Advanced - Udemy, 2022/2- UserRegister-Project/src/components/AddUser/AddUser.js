import React, { useState } from "react";
import "./AddUser.css";

export default function AddUser() {
  const [name, setName] = useState("");
  const [surname, setSurname] = useState("");
  const [email, setEmail] = useState("");

  const onSubmitHandler = (event) => {
    event.preventDefault();

    const user = { name, surname, email };

    fetch("https://reqres.in/api/users", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(user),
    }).then((res) => {
      if (res.ok) {
        setName("");
        setSurname("");
        setEmail("");
        alert("User successfully registered!");
      }
    });
  };

  return (
    <div className="AddUser">
      <h2>Register User</h2>
      <form onSubmit={onSubmitHandler}>
        <div className="Line">
          <div className="Row">
            <label>Name</label>
            <input
              type="text"
              name="name"
              value={name}
              onChange={(event) => setName(event.target.value)}
              required
            ></input>
          </div>
          <div className="Row">
            <label>Surname</label>
            <input
              type="text"
              name="surname"
              value={surname}
              onChange={(event) => setSurname(event.target.value)}
              required
            ></input>
          </div>
        </div>
        <div className="Line">
          <div className="Row">
            <label>Email</label>
            <input
              type="email"
              name="email"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
              required
            ></input>
          </div>
        </div>
        <button type="submit">Register</button>
      </form>
    </div>
  );
}
