const box = document.getElementById('box')
const boxButton = document.getElementById('boxButton')

let size = 500

boxButton.addEventListener('click', () => {
    size += 10
    box.style.width = size + "px"
    box.style.height = size + "px"
})