from sqlalchemy import Boolean, Column, Float, Integer, String, Text

from .database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True, nullable=False)
    original_title = Column(String, nullable=True)
    description = Column(Text, nullable=False)
    full_description = Column(Text, nullable=False)
    image_url = Column(String, nullable=False)
    cover_url = Column(String, nullable=True)
    movie_type = Column(String, default="movie", nullable=False)
    genre = Column(String, default="action", nullable=False)
    rating = Column(Float, default=0.0, nullable=False)
    year = Column(Integer, default=2024, nullable=False)
    duration = Column(String, default="2h 0m", nullable=False)
    views = Column(Integer, default=0, nullable=False)
    featured = Column(Boolean, default=False, nullable=False)
