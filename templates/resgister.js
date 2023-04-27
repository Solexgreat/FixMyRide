const registerForm = document.getElementById('register-form');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');

registerForm.addEventListener('click', async (event) => {
  event.preventDefault();

  const EmailCheck = emailInput.value.trim()
  if(!EmailCheck || !EmailCheck.include('@')) {
    alert('Enter a valid email address')
    return;
  }

  const PasswordCheck = passwordInput.value.trim()
  if(PasswordCheck < 8) {
    alert('Password must be eight character and Above')
    return;
  }

  const formData = new FormData(resgister-form)

  const response = await fetch('http://localhost:5000/register', {
    method: 'POST',
    body: formData,
  });

  if (response.ok) {
    const data = await response.json();
    alert(data.error_msg);
  }
});