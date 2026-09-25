from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager

from .crud import get_featured_movies, get_movie_by_id, get_movies, seed_movies
from .database import Base, SessionLocal, engine
from .models import Movie


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_movies(db)
    finally:
        db.close()
    yield


app = FastAPI(title="Flakes Movie Platform", lifespan=lifespan)

app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/js", StaticFiles(directory="js"), name="js")

if __name__ != "__main__":
    try:
        app.mount("/img", StaticFiles(directory="img"), name="img")
    except Exception:
        pass


templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    db = SessionLocal()
    try:
        movies = get_movies(db, movie_type="movie")
        series = get_movies(db, movie_type="series")
        featured = get_featured_movies(db)
        return templates.TemplateResponse(
            "home.html",
            {
                "request": request,
                "featured": featured,
                "movies": movies[:7],
                "series": series[:7],
                "trending": sorted(movies + series, key=lambda m: m.views, reverse=True)[:7],
            },
        )
    finally:
        db.close()


@app.get("/movies", response_class=HTMLResponse)
async def movies_page(request: Request):
    db = SessionLocal()
    try:
        movies = get_movies(db, movie_type="movie")
        return templates.TemplateResponse("movies.html", {"request": request, "movies": movies})
    finally:
        db.close()


@app.get("/series", response_class=HTMLResponse)
async def series_page(request: Request):
    db = SessionLocal()
    try:
        series = get_movies(db, movie_type="series")
        return templates.TemplateResponse("series.html", {"request": request, "series": series})
    finally:
        db.close()


@app.get("/popular", response_class=HTMLResponse)
async def popular_page(request: Request):
    db = SessionLocal()
    try:
        popular = get_movies(db)
        return templates.TemplateResponse("popular.html", {"request": request, "popular": popular})
    finally:
        db.close()


@app.get("/trends", response_class=HTMLResponse)
async def trends_page(request: Request):
    db = SessionLocal()
    try:
        trending = sorted(get_movies(db), key=lambda m: m.views, reverse=True)
        return templates.TemplateResponse("trends.html", {"request": request, "trending": trending})
    finally:
        db.close()


@app.get("/search", response_class=HTMLResponse)
async def search_page(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})


@app.get("/movie/{movie_id}", response_class=HTMLResponse)
async def details_page(request: Request, movie_id: int):
    db = SessionLocal()
    try:
        movie = get_movie_by_id(db, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        return templates.TemplateResponse("details.html", {"request": request, "movie": movie})
    finally:
        db.close()


@app.get("/api/movies")
async def get_movies_api(movie_type: str | None = None, genre: str | None = None, q: str | None = None):
    db = SessionLocal()
    try:
        movies = get_movies(db, movie_type=movie_type, genre=genre, query=q)
        return [
            {
                "id": movie.id,
                "title": movie.title,
                "description": movie.description,
                "full_description": movie.full_description,
                "image_url": movie.image_url,
                "cover_url": movie.cover_url,
                "movie_type": movie.movie_type,
                "genre": movie.genre,
                "rating": movie.rating,
                "year": movie.year,
                "duration": movie.duration,
                "views": movie.views,
                "featured": movie.featured,
            }
            for movie in movies
        ]
    finally:
        db.close()


@app.get("/api/movies/{movie_id}")
async def get_movie_api(movie_id: int):
    db = SessionLocal()
    try:
        movie = get_movie_by_id(db, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        return {
            "id": movie.id,
            "title": movie.title,
            "description": movie.description,
            "full_description": movie.full_description,
            "image_url": movie.image_url,
            "cover_url": movie.cover_url,
            "movie_type": movie.movie_type,
            "genre": movie.genre,
            "rating": movie.rating,
            "year": movie.year,
            "duration": movie.duration,
            "views": movie.views,
            "featured": movie.featured,
        }
    finally:
        db.close()
