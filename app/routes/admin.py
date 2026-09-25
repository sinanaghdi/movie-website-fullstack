from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..models import User, Movie
from ..schemas import MovieCreate, MovieRead, MovieUpdate
from ..crud import create_movie, get_movie_by_id, get_movies, update_movie, delete_movie
from ..dependencies import get_db, get_admin_user

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/movies", response_model=MovieRead)
async def create_movie_admin(
    movie: MovieCreate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_admin_user)
):
    """Create a new movie (admin only)"""
    existing = db.query(Movie).filter(Movie.title == movie.title).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Movie title already exists"
        )
    
    return create_movie(db, movie)


@router.get("/movies", response_model=list[MovieRead])
async def get_all_movies_admin(
    db: Session = Depends(get_db),
    admin: User = Depends(get_admin_user)
):
    """Get all movies for admin dashboard"""
    return db.query(Movie).all()


@router.put("/movies/{movie_id}", response_model=MovieRead)
async def update_movie_admin(
    movie_id: int,
    movie_update: MovieUpdate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_admin_user)
):
    """Update a movie (admin only)"""
    movie = update_movie(db, movie_id, movie_update)
    if not movie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movie not found"
        )
    return movie


@router.delete("/movies/{movie_id}")
async def delete_movie_admin(
    movie_id: int,
    db: Session = Depends(get_db),
    admin: User = Depends(get_admin_user)
):
    """Delete a movie (admin only)"""
    success = delete_movie(db, movie_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movie not found"
        )
    return {"message": "Movie deleted successfully"}
