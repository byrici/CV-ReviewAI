import './App.css';
import { useState } from 'react';
import axios from 'axios';

function App() {
  const [resumeFile, setResumeFile] = useState(null);
  const [jobFile, setJobFile] = useState(null);
  const [optimizedText, setOptimizedText] = useState("");
  const [loading, setLoading] = useState(false);
  

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
      setLoading(true);
      const response = await axios.post("http://localhost:8000/analyze/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setOptimizedText(response.data.optimized_resume);
    } catch (error) {
      console.error("Fehler beim Hochladen:", error);
    }
      finally {
      setLoading(false);
    }
  };

  return (
    <div className="PageWrapper">
      <div className="Navbar">
        <div className="Navbar-Left">
          <div className="Logo">🧠 AI-Review</div>
          <a href="/login">Use Cases</a>
          <a href="/login">Products</a>
          <a href="/login">Pricing</a>
        </div>
        <div className="Navbar-Right">
          <a href="/login" className="Login">Log in</a>
          <a href="/login" className="TryFree">Try for free</a>
        </div>
      </div>

      <div className="App">
      <h1 className="HeroHeadline">Mache deinen Lebenslauf</h1>
      <h1 className="HeroSubline">
        <span className="Colorful orange">Besser</span>,&nbsp;
        <span className="Colorful yellow">Schöner</span>&amp;
        <span className="Colorful teal">Smarter</span> <span className="Colorful white">mit AI</span>
      </h1>
        <h3>
          Die einzige Plattform die du für deinen Lebenslauf brauchst.
        </h3>

        <p>Laden Sie Ihren Lebenslauf hoch</p>
        <label className="Upload-Box">
          <input type="file" accept=".pdf, image/*" onChange={handleResumeChange} />
          <span>{resumeFile ? resumeFile.name : "Datei auswählen"}</span>
        </label>

        <p>Laden Sie jetzt die Stellenbeschreibung hoch</p>
        <label className="Upload-Box">
          <input type="file" accept=".pdf, image/*" onChange={handleJobChange} />
          <span>{jobFile ? jobFile.name : "Datei auswählen"}</span>
        </label>

        <button className="Generieren-Button" onClick={handleSubmit}>
          Jetzt verbessern!
        </button>

        {loading && (
          <div className="ProgressBarWrapper">
            <div className="ProgressBar">
              <div className="ProgressBar-Fill" />
            </div>
          </div>
        )}

        {optimizedText && (
          <div className="Optimized-Output">
            <h2>Optimierter Lebenslauf</h2>
            <pre>{optimizedText}</pre>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
