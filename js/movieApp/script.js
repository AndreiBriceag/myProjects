const API_URL = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=9a760b3717fd329fd14eb85f72d5de32&page=1'
const IMG_PATH = 'https://image.tmdb.org/t/p/w1280'
const SEARCH_API = 'https://api.themoviedb.org/3/search/movie?api_key=9a760b3717fd329fd14eb85f72d5de32&query="'

const maine = document.getElementById('main')
const form = document.getElementById('form')
const search = document.getElementById('search')

//get initial movies
getMovies(API_URL)

async function getMovies(url) {
    const response = await fetch(url)
    const data = await response.json()

    showMovies(data.results)
}

function showMovies(movies) {
    main.innerHTML = ''

    movies.forEach((movie) => {
        const { title, poster_path, vote_average, overview } = movie

        const movieElement = document.createElement('div')
        movieElement.classList.add('movie')

        movieElement.innerHTML = `
            <img src="${IMG_PATH + poster_path}" alt="${title}">
            <div class="movie-info">
                <h3>${title}</h3>
                <span class="${getClassByRate(vote_average)}">${vote_average}</span>
            </div>
            <div class="overview">
                <h3>Overview</h3>
                ${overview}
            </div>
        `
        main.appendChild(movieElement)
    })
}

//create class by the movie rate
function getClassByRate(vote) {
    if(vote >= 8) {
        return 'green'
    } else if(vote >= 5) {
        return "orange"
    } else {
        return 'red'
    }
}

form.addEventListener('submit', (e) => {
    e.preventDefault() //because event linstener is 'submit', so it doesn't submit to the page

    const searchTerm = search.value

    if(searchTerm && searchTerm !== '') {
        getMovies(SEARCH_API + searchTerm)

        search.value = '' //clear search box
    } else {
        window.location.reload() //if we submit with empty value, reload page
    }
})