window.addEventListener("load", function(){
    let scroll = document.querySelector(".scroll");

    window.addEventListener("scroll",e=>{
        if(window.scrollY>500){
            scroll.classList.add("show")
        }else{
            scroll.classList.remove("show")
        }
    })
      
      
    scroll.addEventListener("click",e=>{
        if(scroll.classList.contains("show")){
            window.scrollTo({top:0,behavior:"smooth"})
        }
    })    
    
})


let popupBtn=document.querySelector(".popup-btn")

if(popupBtn){
    var popupwrapper=document.createElement("div");
    popupwrapper.className="wrapper";
    document.body.prepend(popupwrapper)
}

// popupBtn.addEventListener("click",r=>{
//         let popup=popupBtn.nextElementSibling
//         popup.classList.add("show")
//         popupwrapper.classList.add("show")
        
//         let popupclose=document.querySelectorAll(".popup-close")
//         console.log(popupclose)
        
        
//         let popupcloseFunc=e=>{
//             popup.classList.remove("show")
//             popupwrapper.classList.remove("show")
//         }
        
//         popupclose.forEach(pop => {
//             pop.addEventListener("click", popupcloseFunc)
//         })
// })


let hamburger=document.querySelector(".hamburger")
let navmenu=document.querySelector(".nav-menu")

hamburger.addEventListener("click",e=>{
    hamburger.classList.toggle("active")
    navmenu.classList.toggle("active")
})

let navItem=document.querySelectorAll(".nav-item")

navItem.forEach(e=>{
    e.addEventListener("click",()=>{
        hamburger.classList.remove("active")
        navmenu.classList.remove("active")
    })
})