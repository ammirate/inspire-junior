import React, { Component } from "react";

class CategoriesContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  render() {
    return (
      <div className="container">
        <select defaultValue={-1} className="custom-select">
          <option value={-1}>All categories</option>
          {this.props.categories.map(cat => (
            <option key={cat.id} value={cat.id}>
              {cat.name}
            </option>
          ))}
        </select>
      </div>
    );
  }
}

export default CategoriesContainer;
