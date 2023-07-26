const buttons = document.querySelectorAll('.ripple')

buttons.forEach(button => {
    button.addEventListener('click', function (e) { //regular function instead of () => {}
        const x = e.clientX
        const y = e.clientY

        const buttonTop = e.target.offsetTop //where button starts at the top
        const buttonLeft = e.target.offsetLeft //where button starts at the left

        const xInside = x - buttonLeft //positions X and Y where the click happens, inside the button
        const yInside = y - buttonTop

        const circle = document.createElement('span')
        circle.classList.add('circle')
        circle.style.top = yInside + 'px'
        circle.style.left = xInside + 'px'

        this.appendChild(circle) //this. won't work with () => {}, so it has to be a regular function

        setTimeout(() => circle.remove(), 500) //remove span after 500ms, to avoid multiple span being created
    })
})