import React from "react";
import NavBar from "./components/navbar";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <div>
        <NavBar></NavBar>
      </div>
    </Router>
  );
}
