import React, { Component } from "react";

class ArticleContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    const article = this.props.article;

    return (
      <div className="list-group-item">
        <div className="card">
          <div className="card-body">
            <div className="row">
              <div className="col-11">
                <h2 className="card-title"> {article["title"]} </h2>
              </div>
              <div className="col1">
                <span className="badge badge-primary">
                  {article["category"]["name"]}
                </span>
              </div>
            </div>
            <p className="card-text">{article["abstract"]}</p>
          </div>
        </div>
      </div>
    );
  }
}

export default ArticleContainer;
