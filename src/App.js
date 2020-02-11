import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { Box } from "@material-ui/core";

import NavBar from "./components/navbar";
import Footer from "./components/footer";

export default function App() {
  return (
    <Router>
      <div>
        <NavBar></NavBar>
        <Box m={2}>
          <Footer></Footer>
        </Box>
      </div>
    </Router>
  );
}
