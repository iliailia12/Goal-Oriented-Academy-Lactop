        const btn = document.getElementsByClassName("colorChangeBtn")[0]
        const box = document.getElementsByClassName("colorDiv")[0]
        btn.addEventListener('click',()=>{
            box.style.backgroundColor = 'red'
        })