// desplegar el menú en dispositivos pequeños, menú tipo hamburguesa
hamburger = document.querySelector(".hamburger");
hamburger.onclick = function(){
    navbar = document.querySelector(".nav-bar");
    navbar.classList.toggle("active");
}




// active nav link
// const activePage = window.location.pathname;
// console.log(activePage);
// const navLinks = document.querySelectorAll('.nav-bar .nav-links a').forEach(link => {

//     if(link.href.includes(`${activePage}`) && activePage != '/')
//     {
//         console.log(link.href)
//         link.classList.add('active');
//     }
// })