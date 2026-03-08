let number = 1;

const multiplyBtn = document.getElementById("MultiplyBtn");
const numberText = document.getElementById("number");

multiplyBtn.addEventListener("click", () => {
    number = number * 2;
    numberText.textContent = number;
});