import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");

useEffect(() => {
  fetch("https://<your-username>-8000.githubpreview.dev/")
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

  return <h1>{message || "Loading..."}</h1>;
}

export default App;