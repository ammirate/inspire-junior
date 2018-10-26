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
      return <label>No articles</label>;
    }

    return (
      <React.Fragment>
        {this.state.articles.map(article => (
          <ArticleContainer article={article} key={article.id} />
        ))}
      </React.Fragment>
    );
  }
}

export default ArticleListContainer;
