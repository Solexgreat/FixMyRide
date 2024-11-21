import React, { useState } from 'react'

function Appointments() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [phoneNumber, setPhoneNumber] = useState('');


    useEffect(() => {
        fetch('http://localhost:3000//available-times')
            .then(response => response.json())
            .then(data => setTimeSlots(data))
            .catch(error => console.error('Error fetching time slots:', error));
    }, []);

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

                    <label htmlFor='date'>Appointment date</label>
                    <select id='date' type='date' required >
                        <option>
                            {}
                        </option>
                    </select>
                </div>

            </fieldset>
        </form>
    </section>
  )
}

export default Appointments