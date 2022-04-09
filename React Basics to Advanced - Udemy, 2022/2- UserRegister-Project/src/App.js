import React from "react";
import "./App.css";
import { BrowserRouter, NavLink, Switch, Route } from "react-router-dom";
import Users from "./components/Users/Users";
import AddUser from "./components/AddUser/AddUser";
import UserDetails from "./components/UserDetails/UserDetails";
import Home from "./components/Home/Home";

export default function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <header>
          <nav>
            <ul>
              <li>
                <NavLink to="/" exact>
                  Home
                </NavLink>
              </li>
              <li>
                <NavLink to="/users">Registered Users</NavLink>
              </li>
              <li>
                <NavLink to="/register">Register new user</NavLink>
              </li>
            </ul>
          </nav>
        </header>
        <main>
          <Switch>
            <Route path="/" exact>
              <Home />
            </Route>
            <Route path="/users/:id">
              <UserDetails />
            </Route>
            <Route path="/users">
              <Users />
            </Route>
            <Route path="/register">
              <AddUser />
            </Route>
            <Route path="*">
              <h1>404</h1>
              <p>Page not found.</p>
            </Route>
          </Switch>
        </main>
      </div>
    </BrowserRouter>
  );
}
