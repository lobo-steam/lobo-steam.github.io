const puntero = document.querySelector(".puntero");
const navMenu = document.querySelector(".nav-menu");

puntero.addEventListener("click", mobileMenu);

function mobileMenu() {
    puntero.classList.toggle("active");
    navMenu.classList.toggle("active");
}


// when we click on hamburger icon its close 

const navLink = document.querySelectorAll(".nav-link");

navLink.forEach(n => n.addEventListener("click", closeMenu));

function closeMenu() {
    puntero.classList.remove("active");
    navMenu.classList.remove("active");
}