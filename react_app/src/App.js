import React, { Component } from "react";
import "./App.css";
import MainContainer from "./containers/mainContainer";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    console.log("[app] render", this.state);

    return (
      <React.Fragment>
        <MainContainer />
      </React.Fragment>
    );
  }
}

export default App;
