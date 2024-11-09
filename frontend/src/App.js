import React from 'react';
import './App.css';
import './Css-folder/Nav.css';
import './Css-folder/HeroSection.css';
import Nav from './components/Nav';
import HeroSection from './components/HeroSection';

function App() {
  return (
    <div className='container'>
      <Nav/>
      <HeroSection/>
    </div>
  );
}

export default App;
