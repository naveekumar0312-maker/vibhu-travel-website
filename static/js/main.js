document.addEventListener("DOMContentLoaded", () => {

    const items = document.querySelectorAll(".aero-item");

    items.forEach((item)=>{

        item.addEventListener("click",()=>{

            items.forEach((card)=>{

                if(card!==item){

                    card.classList.remove("active");

                }

            });

            item.classList.toggle("active");

        });

    });

});