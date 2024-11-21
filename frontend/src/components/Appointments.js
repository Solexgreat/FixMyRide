import React, { useState } from 'react'

function Appointments() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [phoneNumber, setPhoneNumber] = useState('');
    const [availableMechanics, setAvailableMechanics] = useState([]);
    const [error, setError] = useState(null);


    useEffect(() => {
        fetch('http://localhost:3000//available-times')
            .then(response => response.json())
            .then(data => setTimeSlots(data))
            .catch(error => console.error('Error fetching time slots:', error));
    }, []);

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
            setAvailableSlot(data.available_slot);
            setError(null);
        } catch (err) {
            setError(err.message);
            setAvailableSlot([])
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


  return (
    <section>
        <form>
            <fieldset>
                <div className={'customerDetails'}>
                    <label htmlFor='Name' >Name</label>
                    <input id='Name' type='text' required />

                    <label htmlFor='email' >Email</label>
                    <input id='email' type='text' required />

                    <label htmlFor='phoneNumber' >Phone</label>
                    <input id='email' type='text' required />
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
                    <label htmlFor='time'>Appointment time</label>
                    <select id='time'>
                        <option>
                            {}
                        </option>
                    </select>

                    <label htmlFor='date'>
                        Select date:
                        <input
                        id='date'
                        type='date'
                        value={date}
                         />
                    </label>

                </div>

                <div className='available-mechanics'>
                    <label htmlFor='select-mechanics'></label>
                    <select id='select-mechanics' type=''>
                            {availableMechanics.length > 0 ? (
                                {
                                    availableMechanics.map((mechanics) => (
                                        <option>
                                        {mechanics.name}
                                        </option>
                                    ))
                                }
                            )
                            }
                    </select>
                </div>

            </fieldset>
        </form>
    </section>
  )
}

export default Appointments