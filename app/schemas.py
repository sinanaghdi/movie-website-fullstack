from pydantic import BaseModel, Field
from typing import Optional


class MovieBase(BaseModel):
    title: str
    original_title: Optional[str] = None
    description: str
    full_description: str
    image_url: str
    cover_url: Optional[str] = None
    movie_type: str = Field(default="movie")
    genre: str = Field(default="action")
    rating: float = Field(default=0.0)
    year: int = Field(default=2024)
    duration: str = Field(default="2h 0m")
    views: int = Field(default=0)
    featured: bool = Field(default=False)


class MovieCreate(MovieBase):
    pass


class MovieRead(MovieBase):
    id: int

    class Config:
        from_attributes = True
