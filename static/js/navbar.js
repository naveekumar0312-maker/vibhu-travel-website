
console.log("Navbar JS Loaded");

window.addEventListener("scroll",function(){

    const navbar=document.querySelector(".custom-navbar");

    if(window.scrollY>50){

        navbar.style.background="#000";

        navbar.style.padding="14px 0";

    }

    else{

        navbar.style.background="rgba(0,0,0,.85)";

        navbar.style.padding="18px 0";

    }

});