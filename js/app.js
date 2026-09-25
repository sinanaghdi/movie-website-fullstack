// ===== CONFIG =====
const API_URL = 'http://localhost:8000/api';

// ===== STATE =====
let currentPage = 'home';
let allMovies = [];
let darkMode = false;

// ===== DOM ELEMENTS =====
const pages = document.querySelectorAll('.page');
const menuItems = document.querySelectorAll('.menu-list-item');
const sidebarIcons = document.querySelectorAll('.left-menu-icon');
const toggleBall = document.querySelector('.toggle-ball');
const container = document.querySelector('.container');
const navbarContainer = document.querySelector('.navbar-container');
const sidebar = document.querySelector('.sidebar');

// ===== PAGE NAVIGATION =====
function navigateTo(page) {
  // Hide all pages
  pages.forEach(p => p.classList.remove('active'));
  document.getElementById(`${page}-page`).classList.add('active');

  // Update active menu item
  menuItems.forEach(item => item.classList.remove('active'));
  document.querySelector(`[data-page="${page}"]`).classList.add('active');

  currentPage = page;

  // Load page content
  loadPageContent(page);
}

function navigateToDetails(movieId) {
  const movie = allMovies.find(m => m.id === movieId);
  if (movie) {
    displayMovieDetails(movie);
    navigateTo('details');
  }
}

// ===== LOAD PAGE CONTENT =====
function loadPageContent(page) {
  switch(page) {
    case 'home':
      loadHomePage();
      break;
    case 'movies':
      loadMoviesPage();
      break;
    case 'series':
      loadSeriesPage();
      break;
    case 'popular':
      loadPopularPage();
      break;
    case 'trends':
      loadTrendsPage();
      break;
    case 'search':
      loadSearchPage();
      break;
  }
}

// ===== HOME PAGE =====
function loadHomePage() {
  // Load new releases
  const newReleases = allMovies.filter(m => m.type === 'movie').slice(0, 7);
  renderMovieList('new-releases-list', newReleases);

  // Load trending
  const trending = allMovies.filter(m => m.rating >= 8).slice(0, 7);
  renderMovieList('trending-list', trending);
}

function renderMovieList(containerId, movies) {
  const container = document.getElementById(containerId);
  container.innerHTML = '';
  
  movies.forEach(movie => {
    const item = document.createElement('div');
    item.className = 'movie-list-item';
    item.innerHTML = `
      <img class="movie-list-item-img" src="${movie.image}" alt="${movie.title}" onclick="navigateToDetails(${movie.id})">
      <span class="movie-list-item-title">${movie.title}</span>
      <p class="movie-list-item-desc">${movie.description}</p>
      <button class="movie-list-item-button" onclick="navigateToDetails(${movie.id})">Watch</button>
    `;
    container.appendChild(item);
  });
}

// ===== MOVIES PAGE =====
function loadMoviesPage() {
  const movies = allMovies.filter(m => m.type === 'movie');
  renderMovieGrid('movies-grid', movies);

  // Add event listeners for filters
  const searchInput = document.getElementById('search-input');
  const genreFilter = document.getElementById('genre-filter');

  searchInput.addEventListener('input', (e) => {
    const filtered = movies.filter(m => 
      m.title.toLowerCase().includes(e.target.value.toLowerCase())
    );
    renderMovieGrid('movies-grid', filtered);
  });

  genreFilter.addEventListener('change', (e) => {
    const filtered = e.target.value 
      ? movies.filter(m => m.genre === e.target.value)
      : movies;
    renderMovieGrid('movies-grid', filtered);
  });
}

// ===== SERIES PAGE =====
function loadSeriesPage() {
  const series = allMovies.filter(m => m.type === 'series');
  renderMovieGrid('series-grid', series);
}

// ===== POPULAR PAGE =====
function loadPopularPage() {
  const popular = allMovies.filter(m => m.rating >= 8).sort((a, b) => b.rating - a.rating);
  renderMovieGrid('popular-grid', popular);
}

// ===== TRENDS PAGE =====
function loadTrendsPage() {
  const trends = allMovies.filter(m => m.views >= 1000).sort((a, b) => b.views - a.views);
  renderMovieGrid('trends-grid', trends);
}

// ===== RENDER MOVIE GRID =====
function renderMovieGrid(containerId, movies) {
  const container = document.getElementById(containerId);
  container.innerHTML = '';

  if (movies.length === 0) {
    container.innerHTML = '<p style="grid-column: 1/-1; text-align: center; padding: 40px;">No movies found</p>';
    return;
  }

  movies.forEach(movie => {
    const card = document.createElement('div');
    card.className = 'movie-card';
    card.innerHTML = `
      <img src="${movie.image}" alt="${movie.title}">
      <div class="movie-card-overlay">
        <div class="movie-card-title">${movie.title}</div>
        <div class="movie-card-rating">⭐ ${movie.rating}</div>
        <button class="movie-card-button" onclick="navigateToDetails(${movie.id})">View Details</button>
      </div>
    `;
    container.appendChild(card);
  });
}

// ===== MOVIE DETAILS PAGE =====
function displayMovieDetails(movie) {
  const container = document.getElementById('details-content');
  container.innerHTML = `
    <button class="back-button" onclick="navigateTo('home')">← Back</button>
    <div class="details-header">
      <img src="${movie.image}" alt="${movie.title}" class="details-poster">
      <div class="details-info">
        <h1>${movie.title}</h1>
        <div class="details-meta">
          <div class="meta-item">
            <span class="meta-label">Rating:</span> ${movie.rating}/10
          </div>
          <div class="meta-item">
            <span class="meta-label">Year:</span> ${movie.year || 'N/A'}
          </div>
          <div class="meta-item">
            <span class="meta-label">Type:</span> ${movie.type.charAt(0).toUpperCase() + movie.type.slice(1)}
          </div>
          <div class="meta-item">
            <span class="meta-label">Duration:</span> ${movie.duration || 'N/A'}
          </div>
          <div class="meta-item">
            <span class="meta-label">Genre:</span> ${movie.genre || 'N/A'}
          </div>
        </div>
        <div class="details-description">
          ${movie.fullDescription || movie.description}
        </div>
        <div class="details-actions">
          <button class="details-button play-button" onclick="alert('Playback not implemented yet')">▶ Play Now</button>
          <button class="details-button wishlist-button" onclick="alert('Added to wishlist!')">♥ Add to Wishlist</button>
        </div>
      </div>
    </div>
  `;
}

// ===== SEARCH PAGE =====
function loadSearchPage() {
  const searchInput = document.getElementById('search-input-full');
  const resultsContainer = document.getElementById('search-results');

  searchInput.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase();
    if (query.length === 0) {
      resultsContainer.innerHTML = '';
      return;
    }
    
    const results = allMovies.filter(m => 
      m.title.toLowerCase().includes(query) ||
      m.description.toLowerCase().includes(query)
    );
    renderMovieGrid('search-results', results);
  });
}

// ===== DARK/LIGHT MODE TOGGLE =====
function toggleDarkMode() {
  darkMode = !darkMode;
  const elements = [
    container,
    navbarContainer,
    sidebar,
    document.querySelector('.toggle'),
    toggleBall,
    ...document.querySelectorAll('.movie-list-title'),
    ...document.querySelectorAll('.left-menu-icon'),
    ...document.querySelectorAll('.search-box'),
    ...document.querySelectorAll('.genre-filter'),
    ...document.querySelectorAll('.movie-card')
  ];

  elements.forEach(el => {
    if (el) el.classList.toggle('active');
  });
}

// ===== CAROUSEL/ARROW FUNCTIONALITY =====
function setupCarousels() {
  const arrows = document.querySelectorAll('.arrow');
  const movieLists = document.querySelectorAll('.movie-list');

  arrows.forEach((arrow, i) => {
    if (!movieLists[i]) return;
    
    let clickCounter = 0;
    const itemNumber = movieLists[i].querySelectorAll('img').length;

    arrow.addEventListener('click', () => {
      const ratio = Math.floor(window.innerWidth / 270);
      clickCounter++;

      if (itemNumber - (4 + clickCounter) + (4 - ratio) >= 0) {
        movieLists[i].style.transform = `translateX(${clickCounter * -300}px)`;
      } else {
        movieLists[i].style.transform = 'translateX(0)';
        clickCounter = 0;
      }
    });
  });
}

// ===== EVENT LISTENERS =====
// Menu navigation
menuItems.forEach(item => {
  item.addEventListener('click', () => {
    const page = item.getAttribute('data-page');
    navigateTo(page);
  });
});

// Sidebar navigation
sidebarIcons.forEach(icon => {
  icon.addEventListener('click', () => {
    const page = icon.getAttribute('data-page');
    if (page) navigateTo(page);
  });
});

// Dark mode toggle
toggleBall.addEventListener('click', toggleDarkMode);

// Logo click to home
document.querySelector('.logo').addEventListener('click', () => {
  navigateTo('home');
});

// ===== LOAD INITIAL DATA =====
async function loadMovies() {
  try {
    // For now, use mock data
    // Later, replace with: const response = await fetch(`${API_URL}/movies`);
    allMovies = getMockMovies();
    
    // Load home page by default
    navigateTo('home');
    setupCarousels();
  } catch (error) {
    console.error('Error loading movies:', error);
    // Use mock data as fallback
    allMovies = getMockMovies();
    navigateTo('home');
  }
}

// ===== MOCK DATA (Replace with API calls) =====
function getMockMovies() {
  return [
    {
      id: 1,
      title: "Her",
      description: "A lonely writer develops a relationship with an operating system.",
      fullDescription: "In a near future, a lonely writer develops an unlikely relationship with an advanced artificial intelligence. This sci-fi romantic drama explores themes of connection, love, and what it means to be human.",
      image: "img/1.jpeg",
      type: "movie",
      rating: 8.0,
      year: 2013,
      duration: "2h 6m",
      genre: "sci-fi",
      views: 5000
    },
    {
      id: 2,
      title: "Star Wars",
      description: "A epic space opera with heroes and villains.",
      fullDescription: "Experience the legendary Star Wars saga with stunning visuals and epic storytelling that spans galaxies.",
      image: "img/2.jpeg",
      type: "movie",
      rating: 8.5,
      year: 1977,
      duration: "2h 1m",
      genre: "sci-fi",
      views: 8000
    },
    {
      id: 3,
      title: "1917",
      description: "A young soldier must deliver a message to stop an attack.",
      fullDescription: "Follow a young British soldier on a dangerous mission across no-man's land during WWI to deliver a message that could save thousands of lives.",
      image: "img/4.jpg",
      type: "movie",
      rating: 8.4,
      year: 2019,
      duration: "1h 59m",
      genre: "drama",
      views: 6500
    },
    {
      id: 4,
      title: "Avengers",
      description: "Earth's mightiest heroes battle to save the world.",
      fullDescription: "A team of superheroes unite to battle an alien invasion and save humanity from destruction.",
      image: "img/5.jpg",
      type: "movie",
      rating: 8.0,
      year: 2019,
      duration: "3h 2m",
      genre: "action",
      views: 9000
    },
    {
      id: 5,
      title: "Storm",
      description: "A thrilling action adventure.",
      fullDescription: "An intense action film filled with breathtaking sequences and stunning cinematography.",
      image: "img/3.jpg",
      type: "movie",
      rating: 7.5,
      year: 2017,
      duration: "1h 45m",
      genre: "action",
      views: 4000
    },
    {
      id: 6,
      title: "Breaking Bad",
      description: "A chemistry teacher turns to crime.",
      fullDescription: "A brilliant chemistry teacher, who is struggling to make ends meet, turns to cooking methamphetamine with a former student.",
      image: "img/6.jpg",
      type: "series",
      rating: 9.5,
      year: 2008,
      duration: "5 Seasons",
      genre: "drama",
      views: 10000
    },
    {
      id: 7,
      title: "The Crown",
      description: "The story of the British royal family.",
      fullDescription: "Explore the decades-long reign of Queen Elizabeth II and her fight to maintain the monarchy.",
      image: "img/7.jpg",
      type: "series",
      rating: 8.6,
      year: 2016,
      duration: "6 Seasons",
      genre: "drama",
      views: 7500
    },
    {
      id: 8,
      title: "Stranger Things",
      description: "A mysterious disappearance in a small town.",
      fullDescription: "When a young boy disappears in a 1980s Indiana town, his friends discover secret government experiments and alternate dimensions.",
      image: "img/8.jpg",
      type: "series",
      rating: 8.7,
      year: 2016,
      duration: "4 Seasons",
      genre: "sci-fi",
      views: 8500
    }
  ];
}

// ===== INITIALIZE APP =====
loadMovies();
