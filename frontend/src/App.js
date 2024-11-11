import React from 'react';
import './App.css';
import './Css-folder/Nav.css';
import './Css-folder/why_chose_us.css';
import './Css-folder/HeroSection.css';
import './Css-folder/popularService.css';
import Nav from './components/Nav';
import WhyChooseUs from './components/WhyChooseUs';
import HeroSection from './components/HeroSection';
import ServiceSection from './components/ServiceSection';


function App() {
  return (
    <div className='container'>
      <Nav/>
      <HeroSection/>
      <ServiceSection/>
      <WhyChooseUs/>
    </div>
);
}

export default App;
