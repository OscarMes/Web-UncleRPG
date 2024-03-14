// desplegar el menú en dispositivos pequeños, menú tipo hamburguesa
hamburger = document.querySelector(".hamburger");
hamburger.onclick = function(){
    navbar = document.querySelector(".nav-bar");
    navbar.classList.toggle("active");
}
