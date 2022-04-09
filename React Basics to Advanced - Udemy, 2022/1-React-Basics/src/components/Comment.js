import React from "react";
import { formatRelative } from "date-fns";
import { ptBR } from "date-fns/locale";
import "./Comment.css";
import userImage from "./user.png";

export default function Comment(props) {
  return (
    <div className="Comment">
      <img class="avatar" src={userImage} alt={props.name} />
      <div class="content">
        <h2 class="name">{props.name}</h2>
        <p class="email">{props.email}</p>
        <p class="message">{props.children}</p>
        <p class="date">
          {formatRelative(props.date, new Date(), { locale: ptBR })}
        </p>
        <button onClick={props.onRemove}>&times;</button>
      </div>
    </div>
  );
}
