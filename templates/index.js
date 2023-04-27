const hamburger = document.querySelector(".hamburger-menu");
const navList = document.querySelector(".nav-list");
hamburger.addEventListener("click", ()=> {
    hamburger.classList.toggle("active")
    navList.classList.toggle("show")
})


function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
  
    if (username === "myusername" && password === "mypassword") {
      alert("Login successful!");
    } else {
      alert("Incorrect username or password.");
    }
  }
  