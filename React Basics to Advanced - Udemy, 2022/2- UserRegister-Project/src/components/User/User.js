import React from "react";
import { Link } from "react-router-dom";
import "./User.css";

export default function User(props) {
  return (
    <div className="User">
      <ul>
        <li>
          <strong>ID:</strong> {props.user.id}
        </li>
        <li>
          <strong>Name:</strong> {props.user.nome} {props.user.sobrenome}
        </li>
        <li>
          <strong>Email:</strong> {props.user.email}
        </li>
        <li>
          <Link to={`/users/${props.user.id}`}>Details</Link>
        </li>
      </ul>
      <button onClick={props.removeUser}>&times;</button>
    </div>
  );
}
