// Navbar Scroll
window.addEventListener("scroll", function () {

    const navbar = document.querySelector(".custom-navbar");

    if (window.scrollY > 50) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }

});

// Mobile Navbar Toggle Fix
document.addEventListener("DOMContentLoaded", function () {

    const menu = document.getElementById("mainNavbar");
    const toggler = document.querySelector(".navbar-toggler");

    if (!menu || !toggler) return;

    const bsCollapse = new bootstrap.Collapse(menu, {
        toggle: false
    });

    toggler.addEventListener("click", function (e) {

        e.preventDefault();

        if (menu.classList.contains("show")) {
            bsCollapse.hide();
        } else {
            bsCollapse.show();
        }

    });

});