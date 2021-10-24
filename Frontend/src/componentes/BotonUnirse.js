import React from "react-router-dom";

export default function  BotonUnirse () {
    return (
        <div>
            <button className = "btn btn-dark">
            Unirse
            </button>
        </div>
    );
}

/* const pedirPartidas = async (evento) => {
        evento.preventDefault();
        const resp = await axios.get('http://localhost:8000/partidas/');
        setNombre({partidas: resp.data})
        console.log(resp)
    } */
