import React from 'react';
import './App.css';
import './Css-folder/Nav.css';
import './Css-folder/why_chose_us.css';
import './Css-folder/HeroSection.css';
import './Css-folder/popularService.css';
import './Css-folder/TestimonialSection.css';
import Nav from './components/Nav';
import WhyChooseUs from './components/WhyChooseUs';
import TestimonialSection from './components/TestimonialSection';
import PopularServices from './components/PopularServices';
import Footer from './components/Footer';
// import Main from './components/Main';
import {Routes,  Route, useLocation } from 'react-router-dom';
import HeroSection from './components/HeroSection';
import Appointments from './components/Appointments';


function App() {
  return (
    <div className='container'>
      <Nav/>
      <Layout/>
      <Footer/>
    </div>
);
}

function Layout() {
  const location = useLocation();

  const isAppointmentsPage = location.pathname === '/appointments';

  return (
    <div>
      {/* Show the header and main content only if NoT
      on the appointments page*/}
      {!isAppointmentsPage && (
        <>
          <HeroSection />
          <PopularServices/>
          <WhyChooseUs/>
          <TestimonialSection/>
        </>
      )}

      <Routes>
        {/* <Route path='/' element={<HeroSection/>}></Route> */}
        <Route path='/appointments' element={<Appointments/>}></Route>
      </Routes>
    </div>
  );
}

export default App;
