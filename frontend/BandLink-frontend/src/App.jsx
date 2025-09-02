import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");

useEffect(() => {
  fetch("https://cautious-couscous-v6564494vjq4hp4x-8000.app.github.dev/")
    .then(res => {
      console.log("Response status:", res.status);
      return res.json();
    })
    .then(data => {
      console.log("Received data:", data);
      setMessage(data.message);
    })
    .catch(err => console.error("Fetch error:", err));
}, []);

  return <h1>{message || "Balls"}</h1>;
}

export default App;