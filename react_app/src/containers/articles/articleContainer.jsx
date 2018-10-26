import React, { Component } from "react";

class ArticleContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    const article = this.props.article;

    console.log(this.props.article)

    return (
      <div className="container">
        <h2> {article["title"]} </h2>
        <p className="bg-light">{article["abstract"]}</p>
        <div className="panel-footer">
          <span className="label label-default">{article["category_id"]}</span>
        </div>
      </div>
    );
  }
}

export default ArticleContainer;
