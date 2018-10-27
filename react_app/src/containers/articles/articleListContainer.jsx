import React, { Component } from "react";
import ArticleContainer from "./articleContainer";
import axios from "axios";

class ArticleListContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  componentDidMount() {
    this.refresh();
  }

  refresh() {
    axios.get("http://0.0.0.0:5000/api/articles/").then(resp => {
      console.log("[list] Got articles ", resp.data);
      this.setState({ articles: resp.data });
    });
  }

  render() {
    if (!this.state.articles) {
      return (
        <div className="container">
          <h4>No articles</h4>
        </div>
      );
    }

    return (
      <div className="container list-group">
        {this.state.articles.map(article => (
          <ArticleContainer article={article} key={article.id} />
        ))}
      </div>
    );
  }
}

export default ArticleListContainer;
