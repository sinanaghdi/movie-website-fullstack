# Flakes - Multi-Page Movie Streaming Platform

> A full-stack movie streaming website built with **FastAPI**, **SQLite**, and **Vanilla JavaScript**. Multi-page design with real database persistence and RESTful API endpoints.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-lightblue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Pages & Routes](#pages--routes)
- [Database](#database)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)

---

## ✨ Features

✅ **Multi-Page Architecture**
- Home page with featured content & carousels
- Movies page with filtering & search
- Series page
- Popular page (sorted by views/rating)
- Trends page (trending content)
- Search page with live filtering
- Movie details page with full metadata

✅ **Backend**
- FastAPI REST API
- SQLite database with SQLAlchemy ORM
- 10 pre-seeded movies & series
- CRUD operations for movies
- Search & filter endpoints

✅ **Frontend**
- Responsive design (mobile, tablet, desktop)
- Dark/Light mode toggle
- Smooth page navigation
- Movie carousel with arrow controls
- Movie cards with hover effects
- Clean, modern UI inspired by Netflix/Disney+

✅ **Performance**
- Server-side rendering with Jinja2 templates
- Fast database queries with SQLAlchemy
- Static file serving (CSS, JS)
- Auto-reloading dev server

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | FastAPI 0.115.0 |
| **Runtime** | Python 3.11+ |
| **Database** | SQLite 3 |
| **ORM** | SQLAlchemy 2.0 |
| **Templates** | Jinja2 |
| **Frontend** | HTML5, CSS3, Vanilla JS |
| **Server** | Uvicorn |

---

## 📁 Project Structure

```
movie-website-fullstack/
├── app/
│   ├── __init__.py              # FastAPI app initialization
│   ├── main.py                  # Route handlers & page views
│   ├── database.py              # SQLAlchemy setup & session
│   ├── models.py                # Movie database model
│   ├── schemas.py               # Pydantic schemas (validation)
│   └── crud.py                  # Database CRUD operations
├── templates/
│   ├── base.html                # Base template (navbar, sidebar)
│   ├── home.html                # Home page (featured & carousels)
│   ├── movies.html              # Movies listing page
│   ├── series.html              # Series listing page
│   ├── popular.html             # Popular content (sorted by views)
│   ├── trends.html              # Trending content (this week)
│   ├── search.html              # Search results page
│   └── details.html             # Movie/series details page
├── css/
│   └── style.css                # Global styles (responsive)
├── js/
│   └── app.js                   # Frontend interactivity
├── main.py                      # Entry point (runs Uvicorn)
├── requirements.txt             # Python dependencies
├── movies.db                    # SQLite database (auto-created)
└── README.md                    # This file
```

---

## 🚀 Installation

### Prerequisites
- Python 3.11 or higher
- Git
- Virtual environment tool (venv, conda, etc.)

### Step 1: Clone the Repository

```bash
git clone https://github.com/sinanaghdi/movie-website-fullstack.git
cd movie-website-fullstack
```

### Step 2: Create Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**On Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- fastapi==0.115.0
- uvicorn[standard]==0.30.6
- sqlalchemy==2.0.35
- jinja2==3.1.4
- pydantic==2.9.2

---

## ▶️ Running the Application

### Start the Server

```bash
python main.py
```

**Expected output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

### Access the Application

Open your browser and navigate to:
```
http://localhost:8000
```

### Stop the Server

Press `Ctrl+C` in your terminal.

---

## 🔌 API Endpoints

All API endpoints return JSON data. Use these for integrating with external apps or building a separate frontend.

### Movies

**Get all movies (with optional filters)**
```http
GET /api/movies
```
Query parameters:
- `movie_type` (optional): `"movie"` or `"series"`
- `genre` (optional): `"action"`, `"drama"`, `"sci-fi"`, `"comedy"`
- `q` (optional): Search query (searches title & description)

**Example:**
```bash
curl "http://localhost:8000/api/movies?movie_type=movie&genre=action"
curl "http://localhost:8000/api/movies?q=Matrix"
```

**Response:**
```json
[
  {
    "id": 1,
    "title": "Her",
    "description": "A lonely writer falls in love with an AI assistant.",
    "full_description": "...",
    "image_url": "https://...",
    "movie_type": "movie",
    "genre": "sci-fi",
    "rating": 8.4,
    "year": 2013,
    "duration": "2h 6m",
    "views": 5200,
    "featured": true
  },
  ...
]
```

**Get a specific movie**
```http
GET /api/movies/{movie_id}
```

**Example:**
```bash
curl "http://localhost:8000/api/movies/1"
```

**Response:**
```json
{
  "id": 1,
  "title": "Her",
  "description": "A lonely writer falls in love with an AI assistant.",
  "full_description": "In a near-future Los Angeles, Theodore Twombly navigates life after a painful breakup while developing a deep connection with Samantha, an advanced operating system designed to understand and respond to human emotions.",
  "image_url": "https://...",
  "cover_url": "https://...",
  "movie_type": "movie",
  "genre": "sci-fi",
  "rating": 8.4,
  "year": 2013,
  "duration": "2h 6m",
  "views": 5200,
  "featured": true
}
```

---

## 🌐 Pages & Routes

| Page | Route | Description |
|------|-------|-------------|
| Home | `/` | Featured content, new releases, trending |
| Movies | `/movies` | All movies with search & genre filter |
| Series | `/series` | All TV series |
| Popular | `/popular` | Sorted by views & rating |
| Trends | `/trends` | Trending this week (by views) |
| Search | `/search` | Live search results |
| Details | `/movie/{id}` | Full movie/series details |

---

## 💾 Database

### Database File
- **Location:** `movies.db` (created automatically on first run)
- **Type:** SQLite
- **Engine:** SQLAlchemy ORM

### Movie Model

The `Movie` table has the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Primary key (auto-increment) |
| `title` | String | Movie/series title (unique) |
| `original_title` | String | Original title (optional) |
| `description` | Text | Short description |
| `full_description` | Text | Full detailed description |
| `image_url` | String | Poster image URL |
| `cover_url` | String | Cover image URL (optional) |
| `movie_type` | String | `"movie"` or `"series"` |
| `genre` | String | Genre (`"action"`, `"drama"`, `"sci-fi"`, etc.) |
| `rating` | Float | IMDb-style rating (0.0-10.0) |
| `year` | Integer | Release year |
| `duration` | String | Duration (e.g., `"2h 6m"`, `"5 Seasons"`) |
| `views` | Integer | View count |
| `featured` | Boolean | Featured on home page |

### Seeded Data

The database is automatically seeded with 10 movies on first run:
1. **Her** (Movie, Sci-Fi, Rating: 8.4)
2. **Star Wars** (Movie, Sci-Fi, Rating: 8.7)
3. **1917** (Movie, Drama, Rating: 8.4)
4. **Avengers** (Movie, Action, Rating: 8.1)
5. **Storm** (Movie, Action, Rating: 7.5)
6. **Breaking Bad** (Series, Drama, Rating: 9.5)
7. **The Crown** (Series, Drama, Rating: 8.7)
8. **Stranger Things** (Series, Sci-Fi, Rating: 8.8)
9. **The Matrix** (Movie, Sci-Fi, Rating: 8.7)
10. **The Dark Knight** (Movie, Action, Rating: 9.0)

### Adding More Movies

You can add movies programmatically or directly via Python:

```python
from app.database import SessionLocal
from app.models import Movie

db = SessionLocal()
new_movie = Movie(
    title="Inception",
    description="A mind-bending thriller",
    full_description="...",
    image_url="https://...",
    movie_type="movie",
    genre="sci-fi",
    rating=8.8,
    year=2010,
    duration="2h 28m",
    views=12000,
    featured=True
)
db.add(new_movie)
db.commit()
db.close()
```

---

## 🎨 Customization

### Changing Colors

Edit `css/style.css` to change the theme color from green (`#4dbf00`) to your preferred color:

```css
/* Find and replace all instances of: */
color: #4dbf00;          /* Primary green */
background-color: #4dbf00;
border-color: #4dbf00;

/* With your color, e.g., blue: */
color: #0066ff;
```

### Changing Fonts

Edit the Roboto & Sen font imports in `templates/base.html`:

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
```

### Adding More Movies

1. Add entries to `app/crud.py` in the `seed_movies()` function, or
2. Use the Python script above to add via API

### Changing Featured Movies

Set the `featured=True` flag on movies in the database. Featured movies appear on the home page banner.

---

## 🐛 Troubleshooting

### Issue: Port 8000 is already in use
**Solution:** Use a different port:
```bash
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

### Issue: `ModuleNotFoundError: No module named 'fastapi'`
**Solution:** Make sure your virtual environment is activated and dependencies are installed:
```bash
source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### Issue: Database file not created
**Solution:** Delete `movies.db` and restart the app. It will auto-create and seed.
```bash
rm movies.db
python main.py
```

### Issue: Images not loading
**Solution:** The project uses external image URLs from Unsplash. Make sure you have internet connection. To use local images:
1. Add images to `img/` folder
2. Update `image_url` in database entries to `"/img/filename.jpg"`

---

## 🚀 Future Enhancements

Here are features you can add:

- [ ] **User Authentication** - Login/signup with JWT tokens
- [ ] **Watchlist** - Save favorite movies (requires user model)
- [ ] **Ratings & Reviews** - User reviews and ratings
- [ ] **Admin Panel** - Add/edit/delete movies via web UI
- [ ] **Video Playback** - Integrate with video streaming (HLS/DASH)
- [ ] **Favorites** - Heart/save movies (requires user model)
- [ ] **Pagination** - Handle large movie lists efficiently
- [ ] **Advanced Filters** - Filter by year, duration, language
- [ ] **Recommendations** - ML-based suggestions
- [ ] **Database Backup** - Automated backups
- [ ] **Deployment** - Docker, AWS/Heroku/Railway deployment
- [ ] **API Documentation** - Auto-generated Swagger UI (already available at `/docs`)

---

## 📚 Learn More

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
- [Jinja2 Templates](https://jinja.palletsprojects.com/)
- [Uvicorn Server](https://www.uvicorn.org/)

---

## 📝 File Descriptions

### Backend Files

**`app/__init__.py`** - FastAPI app setup with static file mounting and template configuration

**`app/main.py`** - Route handlers for all pages (home, movies, series, etc.) and API endpoints

**`app/database.py`** - SQLAlchemy engine, session factory, and Base declarative model

**`app/models.py`** - Movie SQLAlchemy model (database schema)

**`app/schemas.py`** - Pydantic schemas for request/response validation

**`app/crud.py`** - Database operations (get_movies, get_movie_by_id, seed_movies, filters)

**`main.py`** - Application entry point (runs Uvicorn server)

### Frontend Files

**`templates/base.html`** - Base layout with navbar, sidebar, toggle (used by all pages)

**`templates/home.html`** - Home page with featured content and carousels

**`templates/movies.html`** - Movies listing with search & genre filter

**`templates/series.html`** - Series listing

**`templates/popular.html`** - Popular content sorted by views

**`templates/trends.html`** - Trending content sorted by views

**`templates/search.html`** - Live search results (fetches from `/api/movies`)

**`templates/details.html`** - Movie/series detail page

**`css/style.css`** - Global styles (responsive design, dark/light mode)

**`js/app.js`** - Frontend interactivity (dark mode toggle, carousel controls)

---

## 📄 License

MIT License - Feel free to use this project for personal or commercial purposes.

---

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

---

## 📞 Support

If you encounter any issues or have questions, feel free to open an issue on GitHub.

---

**Created by:** Sina Naqdi  
**Repository:** https://github.com/sinanaghdi/movie-website-fullstack  
**Last Updated:** 2026-09-25
