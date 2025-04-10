import './App.css';

function App() {
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
        <input type="file" accept="image/*" />
        <span>Datei auswählen</span>
      </label>


      <p className="Text-Stellenbeschreibung-Hochladen">
        Laden Sie jetzt die Stellenbeschreibung hoch
      </p>
      <label className="Upload-Box">
        <input type="file" accept="image/*" />
        <span>Datei auswählen</span>
      </label>

      <button className="Generieren-Button">Jetzt verbessern!</button>
    </div>
  );
}

export default App;
