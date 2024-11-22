import React, { useEffect, useState } from 'react'

function Appointments() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [phoneNumber, setPhoneNumber] = useState('');
    const [date, setDate] = useState("");
    const [time, setTime] = useState("");
    const [availableMechanics, setAvailableMechanics] = useState([]);
    const [availableSlots, setAvailableSlots] = useState([]);
    const [services, setServices] = useState([]);
    const [categories, setCategories] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        if (date){
            fetchAvailableTime()
        }
    }, [date])

    useEffect(() => {
        if (date && time){
            fetchAvailableMechanics()
        }
    }, [time])

    useEffect(() => {
        fetchCategories
    }, [])

    useEffect(() => {
        if (categories){
            fetchAvailableMechanics()
        }
    }, [time])

    const fetchAvailableTime = async () => {
        try{
            const response = await fetch(
                `http://localhost:3000/appointments/available-slots?date=${date}`
            );

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || "failed to fetch data")
            }

            const data = await response.json();
            setAvailableSlots(data.available_slot);
            setError(null);
        } catch (err) {
            setError(err.message);
            setAvailableSlots([])
        }
    }

    const fetchAvailableMechanics = async () => {
        try {
          const response = await fetch(
            `http://localhost:3000/appointments/available-mechanics?date=${date}&time=${time}`
          );

          if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || "Failed to fetch data");
          }

          const data = await response.json();
          setAvailableMechanics(data.available_mechanics);
          setError(null); // Clear previous errors
        } catch (err) {
          setError(err.message);
          setAvailableMechanics([]); // Clear results if there's an error
        }
      };

    const fetchServices = async () => {
        try {
            const response = await fetch(
                `http://localhost:3000/services/service`
            );

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || "Failed to fetch data");
              }

            const data = await response.json();
            setServices(data.services);
            setError(null); // Clear previous errors
        } catch (err) {
            setError(err.message);
            setServices([]);
        }
    }

    const fetchCategories = async () => {
        try {
            const response = await fetch(
                `http://localhost:3000/services/categories`
            );

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || "Failed to fetch data");
              }

            const data = await response.json();
            setServices(data.categories);
            setError(null); // Clear previous errors
        } catch (err) {
            setError(err.message);
            setServices([]);
        }
    }

    const handleSubmit = (e) => {
        e.preventDefault();
    }


  return (
    <section>
        <form onSubmit={handleSubmit}>
            <fieldset>
                <div className={'customerDetails'}>
                    <label htmlFor='Name' >Name</label>
                    <input id='Name'
                    type='text'
                    value={name}
                    onChange={(e) => setName(e.target.value)}  required />

                    <label htmlFor='email' >Email</label>
                    <input id='email'
                    type='text'
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required />

                    <label htmlFor='phoneNumber' >Phone</label>
                    <input id='email'
                    type='text'
                    onChange={(e) => setPhoneNumber(e.target.value)}
                    required />
                </div>

                <div className='category-services'>
                    <label htmlFor='category'> Category </label>
                    <select id='category'>
                        <option>
                            {}
                        </option>
                    </select>

                    <label htmlFor='Service-Type'>Service Type </label>
                    <select id='Service-Type'>
                        <option>
                            {}
                        </option>
                    </select>
                </div>

                <div className='time-date'>
                <label htmlFor='date'>
                        Select date:
                        <input
                        id='date'
                        type='date'
                        value={date}
                         />
                    </label>

                    <label htmlFor='time'>select Time</label>
                    <select id='time'
                    onChange={(e) => setTimeout(e.target.value)}
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