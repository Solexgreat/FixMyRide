const loginForm = document.getElementById('login-form');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');

loginForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const EmailCheck = emailInput.value.trim()
  if(!EmailCheck || !EmailCheck.include('@')) {
    alert('Enter a valid email address')
    return;
  }

  const PasswordCheck = passwordInput.value.trim()
  if(!PasswordCheck) {
    alert('Enter a valid password')
    return;
  }

  const formData = new FormData(loginForm);

  const response = await fetch('/sessions', {
    method: 'POST',
    body: formData
  });

  if (response.ok) {
    const data = await response.json();
    alert(data.message);
    window.location.href = '/index.html';
  } else {
    alert('Invalid email or password');
  }
});