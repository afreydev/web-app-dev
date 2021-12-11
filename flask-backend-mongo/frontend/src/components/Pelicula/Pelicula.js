import "./Pelicula.css";
import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import configData from "../../config.json";

function Pelicula() {
  const { id } = useParams();

  const [pelicula, setPelicula] = useState(undefined);

  useEffect(() => {
    fetch(`${configData.SERVER_URL}/movies/${id}`)
      .then((response) => response.json())
      .then((data) => setPelicula(data));
  }, [id]);

  if (!pelicula) return null;

  return (
    <article id="pelicula">
      <h1 className="mb-3">
        <i className="fas fa-film"></i> {pelicula.titulo}
      </h1>
      <div className="row">
        <div className="col-lg-4 col-xl-5">
          <img className="poster" src={pelicula.imagen} alt={pelicula.titulo} />
        </div>
        <div className="col-lg-8 col-xl-7">
          <p className="calificacion">
            <i className="fas fa-star"></i> 7.5
          </p>
          <p className="sinopsis">{pelicula.sinopsis}</p>
          <p className="director">
            <span className="label">Director:</span>{" "}
            <a href="/">{pelicula.director}</a>
          </p>
          <p className="actores">
            <span className="label">Actores:</span>
          </p>
          <ul>
            {pelicula.actores.split(",").map((actor) => {
              return (
                <li key={actor}>
                  <a href="/">{actor}</a>
                </li>
              );
            })}
          </ul>
        </div>
      </div>
    </article>
  );
}

export default Pelicula;
