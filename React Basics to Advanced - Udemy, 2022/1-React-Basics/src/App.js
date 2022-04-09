import React, { Component } from "react";
import "./App.css";

import Comment from "./components/Comment";

class App extends Component {
  state = {
    comments: [
      {
        name: "João",
        email: "joao@mail.com",
        date: new Date(2020, 3, 19, 17, 30, 0),
        message: "Hello, how are you ?",
      },
      {
        name: "Pedro",
        email: "pedro@mail.com",
        date: new Date(2020, 3, 22, 12, 15, 0),
        message: "Hi, I'm fine :)",
      },
    ],
    newComment: {
      name: "",
      email: "",
      message: "",
    },
  };

  addComment = (event) => {
    event.preventDefault();
    const newComment = { ...this.state.newComment, date: new Date() };
    this.setState({
      comments: [...this.state.comments, newComment],
      newComment: { name: "", email: "", message: "" },
    });
  };

  removeComment = (comment) => {
    let list = this.state.comments;
    list = list.filter((c) => c !== comment);
    this.setState({ comments: list });
  };

  digit = (event) => {
    const { name, value } = event.target;
    this.setState({
      newComment: { ...this.state.newComment, [name]: value },
    });
  };

  render() {
    return (
      <div className="App">
        <h1>My Project</h1>
        {this.state.comments.map((comment, index) => (
          <Comment
            key={index}
            name={comment.name}
            email={comment.email}
            date={comment.date}
            onRemove={this.removeComment.bind(this, comment)}
          >
            {comment.message}
          </Comment>
        ))}

        <form
          method="post"
          onSubmit={this.addComment}
          className="New-Comment"
        >
          <h2>Add comment</h2>
          <div>
            <input
              type="text"
              name="name"
              value={this.state.newComment.name}
              onChange={this.digit}
              required
              placeholder="Insert your name"
            />
          </div>
          <div>
            <input
              type="email"
              name="email"
              value={this.state.newComment.email}
              onChange={this.digit}
              required
              placeholder="Insert your email"
            />
          </div>
          <div>
            <textarea
              name="message"
              value={this.state.newComment.message}
              onChange={this.digit}
              required
              rows="4"
            />
          </div>
          <button type="submit">Add comment</button>
        </form>
      </div>
    );
  }
}

export default App;
