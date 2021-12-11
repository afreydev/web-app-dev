import { useContext, useState } from "react";
import { UserContext } from "../../contexts/UserContext";
import { useHistory } from "react-router-dom";
import "./Login.css";

// async function login(credenciales) {
//   return fetch("http://localhost:8080/login", {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json'
//     },
//     body: JSON.stringify(credenciales)
//   }).then(response => response.json())
// }

async function login(credenciales) {
  return {
    name: "Andrés",
    token: "12345",
  };
}

function Login() {
  const { setUser } = useContext(UserContext);

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const history = useHistory();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const userInfo = await login({
      username,
      password,
    });
    userInfo.isLoggedIn = true;

    console.log(userInfo);
    setUser(userInfo);
    localStorage.setItem("user", JSON.stringify(userInfo));
    history.push("/");
  };

  return (
    <div className="d-flex justify-content-center">
      <form className="text-white" onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="exampleInputEmail1" className="form-label">
            Email
          </label>
          <input
            type="email"
            className="form-control"
            id="exampleInputEmail1"
            aria-describedby="emailHelp"
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="exampleInputPassword1" className="form-label">
            Contraseña
          </label>
          <input
            type="password"
            className="form-control"
            id="exampleInputPassword1"
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button type="submit" className="btn">
          Iniciar sesión
        </button>
      </form>
    </div>
  );
}

export default Login;
