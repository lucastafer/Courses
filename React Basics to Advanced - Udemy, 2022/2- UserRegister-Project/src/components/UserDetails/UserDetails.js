import React, { useState, useEffect } from "react";
import { Link, useParams } from "react-router-dom";

export default function UserDetails() {
  const { id } = useParams();

  const [user, setUser] = useState({});

  useEffect(() => {
    fetch(`https://reqres.in/api/users/${id}`)
      .then((res) => res.json())
      .then((data) => {
        if (data.data) {
          setUser({
            id: data.data.id,
            name: data.data.first_name,
            surname: data.data.last_name,
            email: data.data.email,
            picture: data.data.avatar,
          });
        }
      });
  }, [id]);

  if (user.name !== undefined) {
    return (
      <>
        <h1>
          {user.name} {user.surname}
        </h1>
        <img src={user.picture} alt={user.name} />
        <p>{user.email}</p>
        <Link to="/users">Back</Link>
      </>
    );
  }

  return (
    <>
      <h1>User not found!</h1>
      <Link to="/users">Back</Link>
    </>
  );
}
