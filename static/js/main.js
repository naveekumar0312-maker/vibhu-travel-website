document.addEventListener("DOMContentLoaded", () => {

    const items = document.querySelectorAll(".aero-item");

    items.forEach((item) => {

        item.querySelector(".aero-header").addEventListener("click", () => {

            if (item.classList.contains("active")) {

                item.classList.remove("active");

            } else {

                items.forEach((card) => {

                    card.classList.remove("active");

                });

                item.classList.add("active");

            }

        });

    });

});