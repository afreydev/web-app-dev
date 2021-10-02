import "./Sidenav.css";
import { Link } from "react-router-dom";

function Sidenav({ open, menuClickedFunction }) {
  return (
    /* Side menu */
    <nav id="menu-principal-sidenav" className={open ? "open" : ""}>
      <button
        id="boton-cerrar-menu"
        className="boton-icono"
        onClick={() => menuClickedFunction()}
      >
        <i className="fas fa-times"></i>
      </button>
      <ul>
        <li>
          <Link to="/peliculas">
            <i className="fas fa-film"></i> Peliculas
          </Link>
        </li>
        <li>
          <Link to="/series">
            <i className="fas fa-tv"></i> Series
          </Link>
        </li>
        <li>
          <Link to="/actores">
            <i className="fas fa-user-friends"></i> Actores
          </Link>
        </li>
        <li>
          <Link to="/premios-y-eventos">
            <i className="fas fa-award"></i> Premios y Eventos
          </Link>
        </li>
      </ul>
    </nav>
  );
}

export default Sidenav;
