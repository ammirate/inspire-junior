import React, { Component } from "react";
import axios from "axios";
import NavBar from "./application/navBar";
import ArticleListContainer from "./articles/articleListContainer";
import CategoriesContainer from "./categories/categoriesContainer";

const ARTICLES_API = "http://0.0.0.0:5000/api/articles";
const CATEGORIES_API = "http://0.0.0.0:5000/api/categories";

class MainContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {};
    this.handleOnSelect = this.handleOnChange.bind(this);
  }

  load_articles(cat_id) {
    axios.get(ARTICLES_API + "?category_id=" + cat_id).then(resp => {
      this.setState({ articles: resp.data });
    });
  }

  load_categories() {
    axios.get(CATEGORIES_API).then(resp => {
      this.setState({ categories: resp.data });
    });
  }

  componentWillMount() {
    this.setState({ loading: true });
    // set state to loading
    // request categories
    // request articles
    this.load_categories();
    this.load_articles(-1); // all
  }

  componentDidMount() {
    // remove loading state
    this.setState({ loading: false });
  }

  handleOnChange = event => {
    var cat_id = event.target.value;
    console.log("selected category  " + cat_id);
    this.load_articles(cat_id);
  };

  render() {
    if (this.state.loading) {
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
