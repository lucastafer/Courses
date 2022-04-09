import React, { useState, useEffect } from "react";
import User from "../User/User";

export default function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch("https://reqres.in/api/users")
      .then((res) => res.json())
      .then((data) => {
        const users = data.data.map((user) => ({
          id: user.id,
          name: user.first_name,
          surname: user.last_name,
          email: user.email,
        }));

        setUsers(users);
      });
  }, []);

  const removeUser = (user) => {
    if (
      window.confirm(
        `Are you sure you ant to remove "${user.name} ${user.surname}"?`
      )
    ) {
      fetch(`https://reqres.in/api/users/${user.id}`, {
        method: "DELETE",
      }).then((res) => {
        if (res.ok) {
          setUsers(users.filter((x) => x.id !== user.id));
        }
      });
    }
  };

  return (
    <>
      {users.map((user) => (
        <User key={user.id} user={user} removeUser={() => removeUser(user)} />
      ))}
    </>
  );
}
