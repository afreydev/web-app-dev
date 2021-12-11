import "./GuardarPelicula.css";
import Form from "react-bootstrap/Form";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import React, { useReducer, useEffect } from "react";
import { useParams } from "react-router-dom";
import configData from "../../config.json";

function GuardarPelicula() {
  const guardarPelicula = async (pelicula, idPelicula) => {
    let url = `${configData.SERVER_URL}/movies`;
    if (idPelicula) {
      url = url + "/" + idPelicula;
    }
    delete pelicula._id;
    return fetch(url, {
      method: idPelicula ? "PUT" : "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(pelicula),
    }).then((response) => response.json());
  };

  const formReducer = (state, data) => {
    if (data.isEvent) {
      return {
        ...state,
        [data.name]: data.value,
      };
    }
    return {
      ...data,
    };
  };

  const { id } = useParams();
  const [formData, setFormData] = useReducer(formReducer, {
    titulo: "",
    sinopsis: "",
    director: "",
    calificacion: "",
    imagen: "",
    actores: "",
  });

  useEffect(() => {
    if (id) {
      fetch(`${configData.SERVER_URL}/movies/${id}`)
        .then((response) => response.json())
        .then((data) => setFormData(data));
    }
  }, [id]);

  const handleChange = (event) => {
    setFormData({
      name: event.target.name,
      value: event.target.value,
      isEvent: true,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(formData);

    guardarPelicula(formData, id).then(() => {
      console.log("la pelicula se guardó exitosamente");
      console.log(id);
      if (!id) {
        setFormData({
          titulo: "",
          sinopsis: "",
          director: "",
          calificacion: "",
          imagen: "",
          actores: "",
        });
      }
    });
  };

  return (
    <>
      <h1 className="mb-5">
        <i className="fas fa-film"></i> Guardar Pelicula
      </h1>
      <Form onSubmit={handleSubmit}>
        <Form.Group className="mb-3" controlId="formGroupTitulo">
          <Form.Label>Titulo</Form.Label>
          <Form.Control
            type="text"
            placeholder="Título de la pelicula"
            name="titulo"
            onChange={handleChange}
            value={formData.titulo}
          />
        </Form.Group>
        <Form.Group className="mb-3" controlId="formGroupSinopsis">
          <Form.Label>Sinopsis</Form.Label>
          <Form.Control
            as="textarea"
            rows={3}
            placeholder="Sinopsis de la pelicula"
            name="sinopsis"
            onChange={handleChange}
            value={formData.sinopsis}
          />
        </Form.Group>
        <Row>
          <Form.Group
            as={Col}
            lg="4"
            className="mb-3"
            controlId="formGroupDirector"
          >
            <Form.Label>Director</Form.Label>
            <Form.Control
              type="text"
              placeholder="Director de la pelicula"
              name="director"
              onChange={handleChange}
              value={formData.director}
            />
          </Form.Group>
          <Form.Group
            as={Col}
            sm="12"
            md="6"
            lg="4"
            className="mb-3"
            controlId="formGroupCalificacion"
          >
            <Form.Label>Calificación</Form.Label>
            <Form.Control
              type="number"
              step=".1"
              placeholder="Calificación de la pelicula"
              name="calificacion"
              onChange={handleChange}
              value={formData.calificacion}
            />
          </Form.Group>
          <Form.Group as={Col} className="mb-3" controlId="formGroupImagen">
            <Form.Label>Imagen</Form.Label>
            <Form.Control
              type="text"
              placeholder="Poster de la pelicula"
              name="imagen"
              onChange={handleChange}
              value={formData.imagen}
            />
          </Form.Group>
        </Row>
        <Form.Group className="mb-4" controlId="formGroupActores">
          <Form.Label>Actores</Form.Label>
          <Form.Control
            type="text"
            placeholder="Actores de la pelicula separados por coma"
            name="actores"
            onChange={handleChange}
            value={formData.actores}
          />
        </Form.Group>
        <Button variant="primary" type="submit">
          Guardar Pelicula
        </Button>
      </Form>
    </>
  );
}

export default GuardarPelicula;
