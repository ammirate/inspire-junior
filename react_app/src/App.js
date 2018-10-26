import React, { Component } from "react";
import "./App.css";

import NavBar from "./containers/application/navBar";
import ArticleListContainer from "./containers/articles/articleListContainer";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    console.log("[app] render", this.state);

    return (
      <React.Fragment>
        <div>
          <NavBar />
          <ArticleListContainer />
        </div>
      </React.Fragment>
    );
  }
}

export default App;
