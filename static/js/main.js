let hamburger = document.querySelector('.hamburger');

hamburger.addEventListener('click', ()=>{
    let navbar = document.querySelector('.nav-bar');
    navbar.classList.toggle("active")
})