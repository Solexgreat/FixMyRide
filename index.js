const hamburger = document.querySelector(".hamburger-menu");
const navList = document.querySelector(".nav-list");
hamburger.addEventListener("click", ()=> {
    hamburger.classList.toggle("active")
    navList.classList.toggle("show")

    
})