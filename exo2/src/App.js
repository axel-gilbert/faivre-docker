import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Application Web avec Docker Multi-stage</h1>
        <p>Cette application a été construite en utilisant:</p>
        <ul>
          <li>Un stage de build pour compiler les assets React</li>
          <li>Un stage final avec Nginx pour servir l'application</li>
          <li>Une image optimisée pour la production</li>
        </ul>
      </header>
    </div>
  );
}

export default App; 