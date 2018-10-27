import React, { Component } from "react";
import ArticleContainer from "./articleContainer";
import axios from "axios";

class ArticleListContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    if (this.props.articles.length === 0) {
      return (
        <div className="container">
          <h4>No articles found</h4>
        </div>
      );
    }

    return (
      <div className="container list-group">
        {this.props.articles.map(article => (
          <ArticleContainer article={article} key={article.id} />
        ))}
      </div>
    );
  }
}

export default ArticleListContainer;
