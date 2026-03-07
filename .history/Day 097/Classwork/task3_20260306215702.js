const box = document.getElementById('box')
const boxButton = document.getElementById('boxButton')
const size = 500
box.addEventListener('click',()=>{
    box.style.width = width + 10 + "px"
    box.style.height = height + 10 + "px"
})