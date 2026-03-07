const box = document.getElementById('box')
const boxButton = document.getElementById('boxButton')
const size = 500
box.addEventListener('click',()=>{
    size+=10
    box.style.width = width + 10 + "px"
    box.style.height = height + 10 + "px"
})



const box = document.getElementById('box')
const boxButton = document.getElementById('boxButton')

let size = 50

boxButton.addEventListener('click', () => {
    size += 10
    box.style.width = size + "px"
    box.style.height = size + "px"
})