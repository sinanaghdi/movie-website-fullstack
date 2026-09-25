from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..crud import get_movies, get_movie_by_id, get_featured_movies
from ..dependencies import get_db

router = APIRouter(prefix="/movies", tags=["movies"])


@router.get("/")
async def list_movies(
    movie_type: str | None = None,
    genre: str | None = None,
    q: str | None = None,
    db: Session = Depends(get_db)
):
    """Get movies with optional filters"""
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


@router.get("/{movie_id}")
async def get_movie(movie_id: int, db: Session = Depends(get_db)):
    """Get a specific movie by ID"""
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


@router.get("/featured/all")
async def get_featured(db: Session = Depends(get_db)):
    """Get featured movies"""
    featured = get_featured_movies(db)
    return [
        {
            "id": movie.id,
            "title": movie.title,
            "image_url": movie.image_url,
            "rating": movie.rating,
        }
        for movie in featured
    ]
