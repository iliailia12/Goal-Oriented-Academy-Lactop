const text = document.getElementById('text');
const btn = document.getElementById('BoxBtn');
const box = document.getElementById('box');

btn.addEventListener('click', () => {
    if(text.textContent === 'no'){
        text.textContent = 'yes';
        box.style.backgroundColor = 'black';
    }else{
        text.textContent = 'no';
        box.style.backgroundColor = 'red';
    }
});