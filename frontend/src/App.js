import React from 'react';
import './App.css';
import './Css-folder/Nav.css';
import './Css-folder/why_chose_us.css';
import './Css-folder/HeroSection.css';
import './Css-folder/popularService.css';
import './Css-folder/TestimonialSection.css';
import Nav from './components/Nav';
import WhyChooseUs from './components/WhyChooseUs';
import HeroSection from './components/HeroSection';
import TestimonialSection from './components/TestimonialSection';
import ServiceSection from './components/ServiceSection';
import Footer from './components/Footer';
import Main from './components/Main';


function App() {
  return (
    <div className='container'>
      <Nav/>
      <Main/>
      <HeroSection/>
      <ServiceSection/>
      <WhyChooseUs/>
      <TestimonialSection/>
      <Footer/>
    </div>
);
}

export default App;
