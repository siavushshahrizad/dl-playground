import React, { useState } from "react";

function App() {
  const [inputValue, setInputValue] = useState("");
  const [prediction, setPrediction] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ input_value: parseFloat(inputValue) }),
    });
    const data = await response.json();
    setPrediction(data.prediction);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Input Value:
          <input
            type="number"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
          />
        </label>
        <button type="submit">Predict</button>
      </form>
      {prediction !== null && <p>Prediction: {prediction}</p>}
    </div>
  );
}

export default App;