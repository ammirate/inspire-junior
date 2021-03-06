import React, { Component } from "react";
import ArticleContainer from "./articleContainer";

class ArticleListContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    if (!this.props.articles.length) {
      return (
        <div className="row">
          <div className="col-md-2 offset-md-5">
            <img src="loading.gif" alt="Loading" />
          </div>
        </div>
      );
    }

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
