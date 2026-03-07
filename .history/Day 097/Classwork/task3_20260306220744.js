const box = document.getElementById('box')
const boxButton = document.getElementById('BoxButton')
const size = 500
box.addEventListener('click',()=>{
    size+=10
    box.style.width = width + 10 + "px"
    box.style.height = height + 10 + "px"
})