import React, { useState } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';  // Importamos react-markdown
import './App.css';

function App() {
  const [image, setImage] = useState(null);
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleImageChange = (event) => {
    setImage(event.target.files[0]);
    setResult("");
    setIsSubmitted(false);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!image) {
      alert("Por favor, selecciona una imagen.");
      return;
    }

    const formData = new FormData();
    formData.append("file", image);
    setLoading(true);
    setIsSubmitted(true);

    try {
      const response = await axios.post("http://localhost:8000/upload-image/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setResult(response.data.text);
    } catch (error) {
      console.error("Error al subir la imagen", error);
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setImage(null);
    setResult("");
    setIsSubmitted(false);
  };

  return (
    <div className="container">
      <h1 className="title">Análisis de Factura</h1>

      {!isSubmitted ? (
        <form onSubmit={handleSubmit} className="form">
          <input type="file" onChange={handleImageChange} className="file-input" />
          <button type="submit" className="submit-button" disabled={loading}>
            {loading ? "Cargando..." : "Subir y Procesar"}
          </button>
        </form>
      ) : (
        <button onClick={handleReset} className="reset-button">Subir nueva imagen</button>
      )}

      {/* Mostrar el resultado en formato Markdown */}
      <div className="result-container">
        <ReactMarkdown className="result-text">
          {result || "El resultado aparecerá aquí después de procesar la imagen."}
        </ReactMarkdown>
      </div>
    </div>
  );
}

export default App;
