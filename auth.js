function checkLoginStatus() {
  // Send GET request to backend API endpoint to check if user is authenticated
  fetch('/api/check_login_status')
    .then(response => {
      if (response.ok) {
        // User is authenticated, set loggedIn to true
        loggedIn = true;
      } else {
        // User is not authenticated, set loggedIn to false
        loggedIn = false;
      }
    })
    .catch(error => console.error(error));
}

const appointmentForm = document.getSelection('#appointment_form')
appointmentForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const loggedIn = checkLoginStatus();

  if (!loggedIn) {
    // Display error alert
    const errorAlert = document.createElement('div');
    errorAlert.classList.add('alert', 'alert-danger');
    errorAlert.textContent = 'You must be logged in/registered to create an appointment.';

    // Add error alert to form
    appointmentForm.prepend(errorAlert);

    // Display login/register modal
    $('#login-form').modal('show');
  } else {
    const formData = new FormData(appointmentForm);

    fetch('/appointments', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      // Display success alert
      const successAlert = document.createElement('div');
      successAlert.classList.add('alert', 'alert-success');
      successAlert.textContent = data.message;

      // Add success alert to form
      appointmentForm.prepend(successAlert);

      // Reset form fields
      appointmentForm.reset();
    })
    .catch(error => {
      // Display error alert
      const errorAlert = document.createElement('div');
      errorAlert.classList.add('alert', 'alert-danger');
      errorAlert.textContent = `Error: ${error}`;

      // Add error alert to form
      appointmentForm.prepend(errorAlert);
    });
  }
});
