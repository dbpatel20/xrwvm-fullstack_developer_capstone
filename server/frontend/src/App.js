import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register";  // Import Register component
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      {/* Route for Login */}
      <Route path="/login" element={<LoginPanel />} />

      {/* Route for Register */}
      <Route path="/register" element={<Register />} />
    </Routes>
  );
}

export default App;
