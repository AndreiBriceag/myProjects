const tagsElement = document.getElementById('tags')
const textArea = document.getElementById('textarea')

//clear textArea on page refresh
function refresh() {
    document.getElementById("textarea").value = "";
}
window.onload = refresh;

textArea.focus() //textArea on focus when page loads (type directly without clicking on it)

//create tags pressing comma (,)
textArea.addEventListener('keyup', (e) => {
    createTags(e.target.value)

    if(e.key === 'Enter') {
        setTimeout(() => {e.target.value = ''}, 10) //clear input value, wait a short time (10ms) before randomSelect()

        randomSelect()
    }
})

function createTags(input) {
    const tags = input.split(',')
        .filter(tag => tag.trim() !== '') //filter out the entries that have just blanks (if not equal to an empty string)
        .map(tag => tag.trim()) //trim the input when it contains blanks and characters, also \n

    tagsElement.innerHTML = '' //clear tags so it doesn't pile up

    tags.forEach(tag => {
        const tagEl = document.createElement('span') //create span for every tag split by (,) in textArea
        tagEl.classList.add('tag') //add class of tag to span
        tagEl.innerText = tag //set innerText to what the tag is
        tagsElement.appendChild(tagEl) //append tags to all tagsElement
    })
}

function randomSelect() {
    const times = 30

    //random blinking (highligh + unhighlight)
    const interval = setInterval(() => {
        const randomTag = pickRandomTag()

        highlighTag(randomTag)

        setTimeout(() => {
            unHighlighTag(randomTag)
        }, 100)
    }, 200)

    //after const times of blinking, stop and highlight random tag
    setTimeout(() => {
        clearInterval(interval)

        setTimeout(() => {
            const randomTag = pickRandomTag()

            highlighTag(randomTag)
        }, 100)
    }, times * 100)
}

function pickRandomTag() {
    const tags = document.querySelectorAll('.tag') //tags is an array of '.tag'
    return tags[Math.floor(Math.random() * tags.length)] //random index of tags array
}

function highlighTag(tag) {
    tag.classList.add('highlight')
}

function unHighlighTag(tag) {
    tag.classList.remove('highlight')
}