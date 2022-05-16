import React, { Component } from "react";
import { HashRouter as Router, Route, Routes } from "react-router-dom";
import { Navigate } from "react-router-dom";
import "./App.css";
// the below components will be created shortly
import Login from "./components/Login";
import Groupchat from "./components/Groupchat";
class App extends Component {
  constructor(props) {
    super(props);
  }
render() {
    return (
      <Routes>
        <Navigate exact from="/" to="/login" />
        <Route path="/login" component={Login} />
        <Route path="/chat" component={Groupchat} />
      </Routes>
    );
  }
}
export default App;
