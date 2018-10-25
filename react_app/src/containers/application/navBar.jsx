import React, { Component } from "react";
import { Route, NavLink, HashRouter } from "react-router-dom";

class NavBar extends Component {
  render() {
    return (
      <nav className="navbar navbar-light bg-light">
        <NavLink exact className="navbar-brand" to="/">
          My React App
        </NavLink>
        <NavLink to="/users">Users</NavLink>
        <NavLink to="/contacts">Contacts</NavLink>
      </nav>
    );
  }
}

export default NavBar;
