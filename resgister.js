const registerForm = document.getElementById('register-form');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');

registerForm.addEventListener('submit', async (event) => {
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

});