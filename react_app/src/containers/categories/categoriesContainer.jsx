import React, { Component } from "react";

class CategoriesContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  render() {
    return (
      <div className="container">
        <select defaultValue={undefined} className="custom-select">
          <option value={undefined}>All categories</option>
        </select>
      </div>
    );
  }
}

export default CategoriesContainer;
