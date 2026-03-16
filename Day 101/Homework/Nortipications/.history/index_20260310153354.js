const Main_Form = document.getElementById('Main_Form')
let messige_caunt = 0
const cauntper = document.getElementById('cauntper')


Main_Form.addEventListener('submit',(event)=>{
    event.preventDefault()
    messige_caunt = messige_caunt+1
    cauntper.innerHTML = cauntper
})

cl