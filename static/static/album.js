
let playbuttons=document.querySelectorAll(".album-play");
let song=document.querySelector(".album_music audio");
let processing_bar = document.querySelector(".processing-bar");
let processing = document.querySelector(".processing");
let forward=document.querySelector(".fa-forward");
let backward=document.querySelector(".fa-backward");
let player=document.querySelector(".track-play");
let music_player=document.querySelector(".album_music");
let close=document.querySelector(".close-music");
let album_row=document.querySelectorAll(".album_row");
let name=document.querySelector(".music_name")


function playsong(){
        player.classList.toggle("fa-pause");
        if(player.classList.contains("fa-pause")){
            player.classList.remove("fa-play")
            song.play();
        }else{
            song.pause();
            player.classList.add("fa-play");
        }
        
}

function musicplayerfunc(row,song){
    music_player.classList.add("show");
    player.className="fas track-play fa-pause"
    song.play();
    close.addEventListener("click",()=>{
        music_player.classList.remove("show");
        song.pause();
    })
    let track_name=row.firstElementChild.textContent
    var setname=localStorage.setItem("track_name",track_name)
    var getname=localStorage.getItem("track_name")
    name.textContent=getname
    

}

function loadmusic(audio,play,row){
        let source=audio.src;
        song.src=source;
        for(let i=0;i<playbuttons.length;i++){
            album_row[i].classList.remove("show")
        }
        row.classList.add("show")
        
        
    
}
playbuttons.forEach(play=>{
    play.addEventListener("click",e=>{
        var audio=play.nextElementSibling;
        var row=play.parentElement
        loadmusic(audio,play,row);
        playsong(song);
        musicplayerfunc(row,song);
        
    })
})
player.addEventListener("click",playsong)

song.addEventListener("timeupdate", o => {
        const currentTime = o.target.currentTime;
        const duration = o.target.duration;
        const percent = (currentTime / duration) * 100;
        processing_bar.style.width = `${percent}%`;
        if (processing_bar.style.width=="100%"){
            player.classList.add("fa-play")
    }
})
processing.addEventListener("click", e => {
        
        let container_width = processing.clientWidth;
        let coordinate = e.offsetX;
        let audio_duration = song.duration;
        song.currentTime =(coordinate/container_width)*audio_duration;
        
})


forward.addEventListener("click",()=>{
    song.currentTime+=5
})

backward.addEventListener("click",()=>{
    song.currentTime-=5;
})

for(let j=0;j<playbuttons.length;j++){
    album_row[j].setAttribute("index",j+1)
    

}



