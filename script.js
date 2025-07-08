function breakText() {
    const h1 = document.querySelector(".hero-section, h1")
    const h1Text = h1.innerHTML

    const splittedText = h1Text.split("")
    const halfValue = Math.floor(splittedText.length/2)
    var clutter = ""

    splittedText.forEach((e,id) => {
        if(id<=halfValue){
          clutter += `<span class="a">${e}</span>`  
        }
        else{
            clutter += `<span class="b">${e}</span>`
        }
        
    })

    h1.innerHTML = clutter
}
breakText()

gsap.from("h1 .a",{
    y:100,
    opacity:0,              
    duration:0.6,                   
    delay:0.5,
    stagger:0.15,                    
                        
                    
})

gsap.from("h1 .b",{
    y:80,
    opacity:0,
    duration:0.6,
    delay:0.5,
    stagger:-0.15,
})

gsap.from(".hero-section, button",{
    y:50,
    opacity:0,
    duration:1,
    delay:0.5,
})

function arrow(){
    const plus = document.querySelector(".arrow")
    const container = document.querySelector(".hero")
    
    container.addEventListener("mousemove", (eve) => {
    console.log(eve.x, eve.y);

    plus.style.left = eve.x+"px"; 
    plus.style.top = eve.y+"px";
    
})

}
arrow()

function footerMarque(){
    window.addEventListener("wheel",(eve)=>{
    if(eve.deltaY>0){
        gsap.to(".marque",{
            transform:"translateX(-200%)",
            duration:4,
            repeat:-1,
            ease:"none",
        })
    }
    else{
        gsap.to(".marque",{
            transform:"translateX(0%)",
            duration:4,
            repeat:-1,
            ease:"none",
        })
    }
})
}
footerMarque()