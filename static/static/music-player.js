var audio= document.querySelector("#audio")
let processing_bar = document.querySelector(".processing-bar");
let processing = document.querySelector(".processing");
let playbutton = document.querySelector(".fa-play");
let forward=document.querySelector(".fa-forward")
let backward=document.querySelector(".fa-backward")




    
function playsong(){
    audio.play()
}

function pausesong() {
    audio.pause();
}

playbutton.addEventListener("click",e=>{
    playsong()
    playbutton.classList.toggle("fa-play")
    if (playbutton.classList.contains("fa-play")){
        pausesong()
    }else{
        playsong()
        playbutton.classList.add("fa-pause")
    }

})



audio.addEventListener("timeupdate", o => {
    const currentTime = o.target.currentTime;
    const duration = o.target.duration;
    const percent = (currentTime / duration) * 100;
    processing_bar.style.width = `${percent}%`;
    if (processing_bar.style.width=="100%"){
        playbutton.classList.add("fa-play")
    }
})


processing.addEventListener("click", e => {
        
        let container_width = processing.clientWidth;
        let coordinate = e.offsetX;
        let audio_duration = audio.duration;
        audio.currentTime =(coordinate/container_width)*audio_duration;
        
})


forward.addEventListener("click",e=>{
        audio.currentTime +=5;
})
backward.addEventListener("click",e=>{
        audio.currentTime -=5;
})
