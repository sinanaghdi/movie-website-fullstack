from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..crud import get_movies, get_featured_movies

router = APIRouter(tags=["pages"])
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
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


@router.get("/movies", response_class=HTMLResponse)
async def movies_page(request: Request):
    db = SessionLocal()
    try:
        movies = get_movies(db, movie_type="movie")
        return templates.TemplateResponse("movies.html", {"request": request, "movies": movies})
    finally:
        db.close()


@router.get("/series", response_class=HTMLResponse)
async def series_page(request: Request):
    db = SessionLocal()
    try:
        series = get_movies(db, movie_type="series")
        return templates.TemplateResponse("series.html", {"request": request, "series": series})
    finally:
        db.close()


@router.get("/popular", response_class=HTMLResponse)
async def popular_page(request: Request):
    db = SessionLocal()
    try:
        popular = get_movies(db)
        return templates.TemplateResponse("popular.html", {"request": request, "popular": popular})
    finally:
        db.close()


@router.get("/trends", response_class=HTMLResponse)
async def trends_page(request: Request):
    db = SessionLocal()
    try:
        trending = sorted(get_movies(db), key=lambda m: m.views, reverse=True)
        return templates.TemplateResponse("trends.html", {"request": request, "trending": trending})
    finally:
        db.close()


@router.get("/search", response_class=HTMLResponse)
async def search_page(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})


@router.get("/movie/{movie_id}", response_class=HTMLResponse)
async def details_page(request: Request, movie_id: int):
    db = SessionLocal()
    try:
        from ..crud import get_movie_by_id
        movie = get_movie_by_id(db, movie_id)
        if not movie:
            return templates.TemplateResponse(
                "404.html",
                {"request": request},
                status_code=404
            )
        return templates.TemplateResponse("details.html", {"request": request, "movie": movie})
    finally:
        db.close()
