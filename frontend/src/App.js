import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./Home";
import Ballistics from "./Ballistics";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/ballistics" element={<Ballistics />} />
      </Routes>
    </Router>
  );
}

export default App;