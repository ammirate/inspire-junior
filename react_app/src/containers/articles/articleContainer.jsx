import React, { Component } from "react";

class ArticleContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    const article = this.props.article;

    console.log(this.props.article);

    return (
      <div className="list-group-item">
        <div className="card">
          <div className="card-body">
            <h2 className="card-title"> {article["title"]} </h2>
            <p className="card-text">{article["abstract"]}</p>
            <div className="card-subtitle">
              <span className="label label-default">
                {article["category_id"]} - {article["category"]}
              </span>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default ArticleContainer;
