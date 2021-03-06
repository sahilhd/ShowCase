import React, { Component } from "react";

class Counter extends Component {
  state = {
    count: 0,
    //tags: ["tag1", "tag2", "tag3"],
  };

  /*renderTags() {
    if (this.state.tags.length === 0) return <p> No tags</p>;
    return (
      <ul>
        {this.state.tags.map((tag) => (
          <li key={tag}>{tag}</li>
        ))}
      </ul>
    );
  }
  //styles = {
  // fontSize: 25,
  // fontWeight: "bold",
  //};
  */
  handleIncrement = () => {
    this.setState({ count: this.state.count + 1 });
  };

  render() {
    // console.log("props", this.props);
    return (
      <div>
        {this.props.children}
        <span className={this.getBadgeClasses()}>{this.formatCount()}</span>
        <button
          onClick={() => this.handleIncrement({ id: 1 })}
          className="btn btn-secondary btn-sm"
        >
          Increment
        </button>
        <button
          onClick={() => this.props.onDelete(this.props.id)}
          className="btn btn-danger btn-sm m-2"
        >
          Delete
        </button>
      </div>
    );
  }
  getBadgeClasses() {
    let classes = "badge m-2 badge-";
    classes += this.state.count == 0 ? "warning" : "primary";
    return classes;
  }

  formatCount() {
    const { count } = this.state;
    return count == 0 ? "Zero" : count;
  }
}

export default Counter;
