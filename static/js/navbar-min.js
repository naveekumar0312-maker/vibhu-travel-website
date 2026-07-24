document.addEventListener("DOMContentLoaded", function () {

    const menuToggle = document.getElementById("menuToggle");
    const mainNavbar = document.getElementById("mainNavbar");
    const menuIcon = document.getElementById("menuIcon");

    if (!menuToggle || !mainNavbar) return;

    // Hamburger
    menuToggle.addEventListener("click", function () {

        mainNavbar.classList.toggle("show");

        if (mainNavbar.classList.contains("show")) {

            menuIcon.classList.remove("bi-list");
            menuIcon.classList.add("bi-x");

        } else {

            menuIcon.classList.remove("bi-x");
            menuIcon.classList.add("bi-list");

        }

    });

    // Close menu only for normal links
    document.querySelectorAll(".nav-link:not(#servicesToggle)").forEach(function (link) {

        link.addEventListener("click", function () {

            mainNavbar.classList.remove("show");

            menuIcon.classList.remove("bi-x");
            menuIcon.classList.add("bi-list");

        });

    });

});