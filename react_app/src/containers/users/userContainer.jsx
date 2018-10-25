import React, { Component } from "react";
import axios from "axios";

class UserContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  handleDelete() {
    const { user, onDelete } = this.props;

    let _confirm = window.confirm(
      "Do you really want to delete " +
        user.first_name +
        " " +
        user.last_name +
        "?"
    );
    if (_confirm) {
      axios.delete("http:/0.0.0.0:5000/api/users/" + user.id).then(resp => {
        onDelete();
      });
    }
  }

  render() {
    const user = this.props.user;

    return (
      <tr>
        <td>{user.id}</td>
        <td>
          <a href={user.picture}>
            <img src={user.thumbnail} alt="X" />
          </a>
        </td>

        <td>
          <div>
            {user.first_name} {user.last_name}
            <br />
            {user.birth_date}
          </div>
        </td>

        <td>{user.email}</td>
        <td>
          <button
            className="btn btn-danger btn-sm m-2"
            onClick={event => this.handleDelete()}
          >
            Delete
            <i className="fa fa-trash fa-2x" aria-hidden="true" />
          </button>
        </td>
      </tr>
    );
  }
}

export default UserContainer;
