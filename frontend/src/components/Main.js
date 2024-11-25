import React from 'react'
import HeroSection from './HeroSection';
import Appointments from './Appointments';
import { Routes, Route } from 'react-router-dom';



// /appointments/available_slots

function Main() {




  return (
    <main>
        <Routes>
            <Route path="/" element={<HeroSection/>} />
            <Route path="/appointments" element={<Appointments />} />
        </Routes>
    </main>
  )
}

export default Main