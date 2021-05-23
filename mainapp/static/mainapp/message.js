const submitBtn = document.getElementById('form-btn')
const mainInput = document.getElementById('main-input')

submitBtn.addEventListener('click', () => {
    if (mainInput.value == ''){
        mainInput.placeholder = 'Message cannot be empty!'
    }
    else {
        mainInput.placeholder = 'Enter message here'
    }
})