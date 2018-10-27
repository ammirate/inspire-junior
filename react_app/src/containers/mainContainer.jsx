import React, { Component } from "react";
import NavBar from "./application/navBar";
import ArticleListContainer from "./articles/articleListContainer";
import CategoriesContainer from "./categories/categoriesContainer";

class MainContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  componentWillMount() {
    // set state to loading
    // request categories
    // request articles
  }

  componentDidMount() {
    // remove loading state
  }

  handleOnSelect() {
    // load new articles
  }

  render() {
    return (
      <div>
        <NavBar />
        <CategoriesContainer />
        <hr />
        <ArticleListContainer />
      </div>
    );
  }
}

export default MainContainer;
