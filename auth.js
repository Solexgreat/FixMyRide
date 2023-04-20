const loginForm = document.getElementById('login-form');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');

loginForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  
  const email = emailInput.value;
  const password = passwordInput.value;

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

  const response = await fetch('/sessions', {
    method: 'POST',
    body: JSON.stringify({ email, password }),
    headers: {
      'Content-Type': 'application/json'
    }
  });

  if (response.ok) {
    const data = await response.json();
    alert(data.message);
    window.location.href = '/index.html';
  } else {
    alert('Invalid email or password');
  }
});