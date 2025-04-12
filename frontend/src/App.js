import './App.css';
import { useState } from "react";
import axios from "axios";

function App() {
  const [resumeFile, setResumeFile] = useState(null);
  const [jobFile, setJobFile] = useState(null);
  const [optimizedText, setOptimizedText] = useState(""); // Rückmeldung vom Backend

  const handleResumeChange = (e) => {
    setResumeFile(e.target.files[0]);
  };

  const handleJobChange = (e) => {
    setJobFile(e.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!resumeFile || !jobFile) return;

    const formData = new FormData();
    formData.append("resume", resumeFile);
    formData.append("job_description", jobFile);

    try {
      const response = await axios.post("http://localhost:8000/analyze/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      console.log("Backend-Antwort:", response.data);
      setOptimizedText(response.data.optimized_resume); // Ergebnis im UI anzeigen
    } catch (error) {
      console.error("Fehler beim Hochladen:", error);
    }
  };

  return (
    <div className="App">
      <h1>Review AI</h1>
      <h3>Unsere App analysiert deinen Lebenslauf und gleicht ihn mit der
          gewünschten Stellenanzeige ab. In wenigen Klicks erhältst du eine
          optimierte Version deines Lebenslaufs. Gezielt, professionell und
          individuell auf die Anforderungen des Jobs abgestimmt.
      </h3>
      <p>Laden Sie Ihren Lebenslauf hoch</p>

      <label className="Upload-Box">
        <input type="file" accept=".pdf" onChange={handleResumeChange} />
        <span>{resumeFile ? resumeFile.name : "Datei auswählen"}</span>
      </label>

      <p className="Text-Stellenbeschreibung-Hochladen">
        Laden Sie jetzt die Stellenbeschreibung hoch
      </p>
      <label className="Upload-Box">
        <input type="file" accept=".pdf, image/*" onChange={handleJobChange} />
        <span>{jobFile ? jobFile.name : "Datei auswählen"}</span>
      </label>

      <button className="Generieren-Button" onClick={handleSubmit}>Jetzt verbessern!</button>

      {/* Antwort anzeigen */}
      {optimizedText && (
        <div className="Optimized-Output">
          <h2>Optimierter Lebenslauf</h2>
          <pre>{optimizedText}</pre>
        </div>
      )}

    </div>
  );
}

export default App;
