window.addEventListener("scroll", () => {

    const navbar = document.querySelector(".custom-navbar");

    if (!navbar) return;

    navbar.classList.toggle("scrolled", window.scrollY > 50);

});