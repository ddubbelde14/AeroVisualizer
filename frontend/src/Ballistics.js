import React, { useState } from "react";

function Ballistics() {
  const [v0, setV0] = useState(20);
  const [angle, setAngle] = useState(45);
  const [h0, setH0] = useState(0);
  const [image, setImage] = useState(null);
  const [distance, setDistance] = useState(null);

  const fetchBallistics = () => {
    fetch(`https://aerovisualizer.onrender.com/ballistics?v0=${v0}&angle=${angle}&h0=${h0}`)
      .then(res => res.json())
      .then(data => {
        setImage(data.image);
        setDistance(data.totalDistance);
      });
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Ballistics Simulator</h1>

      <div>
        <label>Initial Speed (m/s): </label>
        <input type="number" value={v0} onChange={e => setV0(e.target.value)} />
      </div>

      <div>
        <label>Launch Angle (°): </label>
        <input type="number" value={angle} onChange={e => setAngle(e.target.value)} />
      </div>

      <div>
        <label>Initial Height (m): </label>
        <input type="number" value={h0} onChange={e => setH0(e.target.value)} />
      </div>

      <button onClick={fetchBallistics} style={{ marginTop: "10px" }}>
        Run Simulation
      </button>

      {image && <img src={`data:image/png;base64,${image}`} alt="Ballistics" style={{ marginTop: "20px" }} />}
      {distance !== null && <p>Total Distance: {distance.toFixed(2)} m</p>}
    </div>
  );
}

export default Ballistics;