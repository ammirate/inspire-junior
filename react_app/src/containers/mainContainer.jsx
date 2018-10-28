import React, { Component } from "react";
import axios from "axios";
import NavBar from "./application/navBar";
import ArticleListContainer from "./articles/articleListContainer";
import CategoriesContainer from "./categories/categoriesContainer";

const baseUrl = "http://0.0.0.0:5555";
const articleApi = baseUrl + "/api/articles";
const categoryApi = baseUrl + "/api/categories";

class MainContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {};
    this.handleOnSelect = this.handleOnChange.bind(this);
  }

  load_articles(cat_id) {
    axios.get(articleApi + "?category_id=" + cat_id).then(resp => {
      this.setState({ articles: resp.data });
    });
  }

  load_categories() {
    axios.get(categoryApi).then(resp => {
      this.setState({ categories: resp.data });
    });
  }

  componentWillMount() {
    this.setState({ loading: true });
    this.load_categories();
    this.load_articles(-1); // all
  }

  componentDidMount() {
    this.setState({ loading: false });
  }

  handleOnChange = event => {
    var cat_id = event.target.value;
    this.load_articles(cat_id);
  };

  render() {
    if (this.state.loading === true) {
      return <h1>Loading...</h1>;
    }
    return (
      <div>
        <NavBar />
        <CategoriesContainer
          categories={this.state.categories || []}
          onChange={this.handleOnChange}
        />
        <hr />
        <ArticleListContainer articles={this.state.articles || []} />
      </div>
    );
  }
}

export default MainContainer;
