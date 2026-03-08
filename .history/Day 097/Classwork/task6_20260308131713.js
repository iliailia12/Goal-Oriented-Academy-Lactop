let number = 1 

const btn = document.getElementById("MultiplyBtn") 
const numberText = document.getElementById("number") 

btn.addEventListener("click", () => {
    number = number * 2 
    numberText.textContent = number 
})