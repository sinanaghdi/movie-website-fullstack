from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime


# ===== MOVIE SCHEMAS =====
class MovieBase(BaseModel):
    title: str
    original_title: Optional[str] = None
    description: str
    full_description: str
    image_url: str
    cover_url: Optional[str] = None
    movie_type: str = Field(default="movie")
    genre: str = Field(default="action")
    rating: float = Field(default=0.0, ge=0.0, le=10.0)
    year: int = Field(default=2024)
    duration: str = Field(default="2h 0m")
    views: int = Field(default=0)
    featured: bool = Field(default=False)


class MovieCreate(MovieBase):
    pass


class MovieUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    full_description: Optional[str] = None
    genre: Optional[str] = None
    rating: Optional[float] = None
    year: Optional[int] = None
    duration: Optional[str] = None
    featured: Optional[bool] = None


class MovieRead(MovieBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# ===== USER SCHEMAS =====
class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(..., min_length=6)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserRead(UserBase):
    id: int
    is_admin: bool
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: Optional[str] = None
    token_type: str = "bearer"
    user: UserRead


class TokenData(BaseModel):
    email: Optional[str] = None
    user_id: Optional[int] = None
