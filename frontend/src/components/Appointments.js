import React, { useEffect, useState, useCallback } from 'react'
import '../Css-folder/Appointment.css'


function Appointments() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [phoneNumber, setPhoneNumber] = useState('');
    const [date, setDate] = useState("");
    const [time, setTime] = useState("");
    const [selectedCategory, setSelectedCategory] = useState("");
    const [selectedServiceId, setSelectedServiceId] = useState("");
    const [availableMechanics, setAvailableMechanics] = useState([]);
    const [availableSlots, setAvailableSlots] = useState([]);
    const [services, setServices] = useState([]);
    const [categories, setCategories] = useState([]);
    const [error, setError] = useState(null);


  const fetchAvailableTime = useCallback(async () => {
    try {
      const response = await fetch(
        `http://localhost:3000/appointments/available-slots?date=${date}`
      );

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Failed to fetch data');
      }

      const data = await response.json();
      setAvailableSlots(data.available_slot);
      setError(null);
    } catch (err) {
      setError(err.message);
      setAvailableSlots([]);
    }
  }, [date]);

  const fetchAvailableMechanics = useCallback(async () => {
    try {
      const response = await fetch(
        `http://localhost:3000/appointments/available-mechanics?date=${date}&time=${time}`
      );

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Failed to fetch data');
      }

      const data = await response.json();
      setAvailableMechanics(data.available_mechanics);
      setError(null);
    } catch (err) {
      setError(err.message);
      setAvailableMechanics([]);
    }
  }, [date, time]);


  const fetchCategories = useCallback(async () => {
    try {
      const response = await fetch(`http://localhost:3000/services/categories`);

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Failed to fetch data');
      }

      const data = await response.json();
      setCategories(data.categories);
      setError(null);
    } catch (err) {
      setError(err.message);
      setCategories([]);
    }
  }, []);


  const fetchServices = useCallback(async () => {
    try {
      const response = await fetch(`http://localhost:3000/services/service_name`);

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Failed to fetch data');
      }

      const data = await response.json();
      setServices(data.services);
      setError(null);
    } catch (err) {
      setError(err.message);
      setServices([]);
    }
  }, []);

  useEffect(() => {
    if (date) fetchAvailableTime();
  }, [date, fetchAvailableTime]);

  useEffect(() => {
    if (date && time) fetchAvailableMechanics();
  }, [time,date, fetchAvailableMechanics]);

  useEffect(() => {
    fetchCategories();
  }, [fetchCategories]);

  useEffect(() => {
    if (selectedCategory) fetchServices();
  }, [selectedCategory, fetchServices]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const appointmentData = {
      date,
      time,
      service_id: selectedServiceId,
      status: 'pending',
    };

    try {
      const response = await fetch(
        'http://localhost:3000/appointments/appointments',
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(appointmentData),
        }
      );

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || 'Failed to create appointment');
      }

      const result = await response.json();
      console.log('Appointment created successfully:', result);
      alert('Appointment successfully created!');
    } catch (error) {
      alert(`Error: ${error.message}`);
    }
  };


  return (
    <section>
        {error && <p className="error-message">{error}</p>}
        <form onSubmit={handleSubmit} className='form-field'>
            <fieldset>
                <div className={'customerDetails'}>
                    <div className='customerDetails-row'>
                        <label htmlFor='Name' >Name</label>
                        <input id='Name'
                        type='text'
                        value={name}
                        onChange={(e) => setName(e.target.value)}  required />
                    </div>

                    <div className='customerDetails-row' >
                        <label htmlFor='email' >Email</label>
                        <input id='email'
                        type='text'
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required />
                    </div>

                    <div className='customerDetails-row' >
                        <label htmlFor='phoneNumber' >Phone</label>
                        <input id='email'
                        type='text'
                        value={phoneNumber}
                        onChange={(e) => setPhoneNumber(e.target.value)}
                        required />
                    </div>
                </div>

                <div className='category-services'>
                    <label htmlFor='category'> Category </label>
                    <select id='category'
                     value={selectedCategory}
                     onChange={(e) => setSelectedCategory(e.target.value)}>
                        <option value="">
                            -- Category --
                        </option>
                        {categories.map((category, index) =>(
                            <option key={index} value={category}>
                                {category}
                            </option>
                        ))}
                    </select>

                    <label htmlFor='Service-Type'>Service Type </label>
                    <select id='Service-Type'
                    value={selectedServiceId}
                    onChange={(e) => setSelectedServiceId(e.target.value)}>
                        <option value="">
                            -- Select services --
                        </option>
                        {services.map((service) => (
                            <option key={service.service_id} value={service.service_id}>
                                {service.name}
                            </option>
                        ))}
                    </select>
                </div>

                <div className='time-date'>
                <label htmlFor='date'>
                        Select date:
                        <input
                        id='date'
                        type='date'
                        value={date}
                        onChange={(e) => setDate(e.target.value)}
                         />
                    </label>

                    <label htmlFor='time'>select Time</label>
                    <select id='time'
                    value={time}
                    onChange={(e) => setTime(e.target.value)}
                    required
                    >
                        <option value="">
                            -- Select-Time --
                        </option>
                            {availableSlots.map((slot, index) =>(
                                <option key={index} value={slot}>
                                    {slot}
                                </option>
                            ))}
                    </select>
                </div>

                <div className='available-mechanics'>
                    <label htmlFor='select-mechanics'></label>
                    <select id='select-mechanics' required>
                        <option value="">-- Select mechanics --</option>
                            {availableMechanics.map((mechanics) => (
                                <option key= {mechanics.user_id} value={mechanics.user_name}>
                                    {mechanics.user_name}
                                </option>
                            ))}
                    </select>
                </div>

            </fieldset>
        </form>
    </section>
  )
}

export default Appointments