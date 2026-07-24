document.addEventListener("DOMContentLoaded", () => {

    const toggle = document.getElementById("menuToggle");
    const menu = document.getElementById("mainNavbar");
    const icon = document.getElementById("menuIcon");

    if (!toggle || !menu) return;

    toggle.addEventListener("click", function () {

        menu.classList.toggle("show");

        if(menu.classList.contains("show")){

            icon.classList.remove("bi-list");
            icon.classList.add("bi-x");

        }else{

            icon.classList.remove("bi-x");
            icon.classList.add("bi-list");

        }

    });

    document.querySelectorAll(".nav-link").forEach(link => {

        link.addEventListener("click", () => {

            menu.classList.remove("show");

            icon.classList.remove("bi-x");
            icon.classList.add("bi-list");

        });

    });

});