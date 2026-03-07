const box = document.getElementById('Box')
const boxButton = document.getElementById('BoxButton')
let  size = 500
let width = 0
let height = +0
box.addEventListener('click',()=>{
    size+=10
    box.style.width = width + 10 + "px"
    box.style.height = height + 10 + "px"
})