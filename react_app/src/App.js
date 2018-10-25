import React, { Component } from "react";
import "./App.css";

import NavBar from "./containers/application/navBar";

import { Route, NavLink, HashRouter } from "react-router-dom";

import ContactsContainer from "./containers/contacts/contactsContainer";
import HomeContainer from "./containers/home/homeContainer";
import UserListContainer from "./containers/users/userListContainer";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    console.log("[app] render", this.state);

    return (
      <React.Fragment>
        <HashRouter>
          <div>
            <NavBar />
            <Route exact path="/" component={HomeContainer} />
            <Route path="/users" component={UserListContainer} />
            <Route path="/contacts" component={ContactsContainer} />
          </div>
        </HashRouter>
      </React.Fragment>
    );
  }
}

export default App;
