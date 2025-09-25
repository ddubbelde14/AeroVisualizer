import React from "react";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Welcome to AeroSolver</h1>
      <p>Click on a solver below.</p>
      <Link to="/ballistics">
        <button>Go to Ballistics Simulator</button>
      </Link>
    </div>
  );
}

export default Home;