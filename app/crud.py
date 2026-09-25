from sqlalchemy.orm import Session

from .models import Movie
from .schemas import MovieCreate


def get_movies(db: Session, movie_type: str | None = None, genre: str | None = None, query: str | None = None):
    movies = db.query(Movie)

    if movie_type:
        movies = movies.filter(Movie.movie_type == movie_type)
    if genre:
        movies = movies.filter(Movie.genre == genre)
    if query:
        q = f"%{query.lower()}%"
        movies = movies.filter(
            (Movie.title.ilike(q)) | (Movie.description.ilike(q)) | (Movie.genre.ilike(q))
        )

    return movies.order_by(Movie.views.desc(), Movie.rating.desc()).all()


def get_movie_by_id(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()


def get_featured_movies(db: Session):
    return db.query(Movie).filter(Movie.featured == True).order_by(Movie.rating.desc()).limit(6).all()


def seed_movies(db: Session):
    if db.query(Movie).count() > 0:
        return

    sample_movies = [
        {
            "title": "Her",
            "original_title": "Her",
            "description": "A lonely writer falls in love with an AI assistant.",
            "full_description": "In a near-future Los Angeles, Theodore Twombly navigates life after a painful breakup while developing a deep connection with Samantha, an advanced operating system designed to understand and respond to human emotions.",
            "image_url": "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?auto=format&fit=crop&w=900&q=80",
            "cover_url": "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?auto=format&fit=crop&w=1400&q=80",
            "movie_type": "movie",
            "genre": "sci-fi",
            "rating": 8.4,
            "year": 2013,
            "duration": "2h 6m",
            "views": 5200,
            "featured": True,
        },
        {
            "title": "Star Wars",
            "original_title": "Star Wars",
            "description": "An epic space saga filled with heroes, villains, and destiny.",
            "full_description": "A young farm boy discovers his destiny in the midst of a galaxy-spanning conflict. With Jedi powers, cosmic battles, and a thrilling rebellion at stake, this film became a global phenomenon.",
            "image_url": "https://images.unsplash.com/photo-1513106580091-1d82408b8cd6?auto=format&fit=crop&w=900&q=80",
            "cover_url": "https://images.unsplash.com/photo-1513106580091-1d82408b8cd6?auto=format&fit=crop&w=1400&q=80",
            "movie_type": "movie",
            "genre": "sci-fi",
            "rating": 8.7,
            "year": 1977,
            "duration": "2h 1m",
            "views": 7600,
            "featured": True,
        },
        {
            "title": "1917",
            "original_title": "1917",
            "description": "A tense World War I mission across enemy territory.",
            "full_description": "Two British soldiers are thrust into a brutal mission across no-man's-land to deliver a warning that could save thousands of lives during a deadly World War I offensive.",
            "image_url": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=900&q=80",
            "cover_url": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=1400&q=80",
            "movie_type": "movie",
            "genre": "drama",
            "rating": 8.4,
            "year": 2019,
            "duration": "1h 59m",
            "views": 6900,
            "featured": True,
        },
        {
            "title": "Avengers",
            "original_title": "Avengers",
            "description": "Earth's mightiest heroes rise to save humanity.",
            "full_description": "When an alien threat emerges, a team of superheroes joins forces to protect the planet from destruction and stop an intergalactic war from causing global devastation.",
            "image_url": "https://images.unsplash.com/photo-1516280440614-37939bbacd81?auto=format&fit=crop&w=900&q=80",
            "cover_url": "https://images.unsplash.com/photo-1516280440614-37939bbacd81?auto=format&fit=crop&w=1400&q=80",
            "movie_type": "movie",
            "genre": "action",
            "rating": 8.1,
            "year": 2019,
            "duration": "3h 2m",
            "views": 8300,
            "featured": False,
        },
        {
            "title": "Storm",
            "original_title": "Storm",
            "description": "A high-impact action thriller in the middle of chaos.",
            "full_description": "When a violent storm system meets a desperate rescue mission, a team of survivors struggles against nature and time to save lives and escape the eye of the disaster.",
            "image_url": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=900&q=80",
            "cover_url": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1400&q=80",
            "movie_type": "movie",
            "genre": "action",
            "rating": 7.5,
            "year": 2017,
            "duration": "1h 45m",
            "views": 4100,
            "featured": False,
        },
        {
            "title": "Breaking Bad",
            "original_title": "Breaking Bad",
            "description": "A chemistry teacher turns to the dark side.",
            "full_description": "Walter White, a brilliant chemistry teacher, transforms from a quiet family man into a feared criminal mastermind after making a terrifying decision with life-changing consequences.",
            "image_url": "https://images.unsplash.com/photo-1524985069026-dd778a71c7b4?auto=format&fit=crop&w=900&q=80",
            "cover_url": "https://images.unsplash.com/photo-1524985069026-dd778a71c7b4?auto=format&fit=crop&w=1400&q=80",
            "movie_type": "series",
            "genre": "drama",
            "rating": 9.5,
            "year": 2008,
            "duration": "5 Seasons",
            "views": 9960,
            "featured": True,
        },
        {
            "title": "The Crown",
            "original_title": "The Crown",
            "description": "The royal story of a nation and an empire.",
            "full_description": "From the postwar years to modern-day Britain, The Crown follows the making of one of the world's most enduring and influential monarchies through history, politics, and family.",
            "image_url": "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=900&q=80",
            "cover_url": "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=1400&q=80",
            "movie_type": "series",
            "genre": "drama",
            "rating": 8.7,
            "year": 2016,
            "duration": "6 Seasons",
            "views": 7200,
            "featured": False,
        },
        {
            "title": "Stranger Things",
            "original_title": "Stranger Things",
            "description": "A small town faces supernatural mysteries.",
            "full_description": "When a young boy disappears, his friends, family, and a small-town sheriff uncover clues tied to secret experiments and a terrifying alternate dimension known as the Upside Down.",
            "image_url": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?auto=format&fit=crop&w=900&q=80",
            "cover_url": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?auto=format&fit=crop&w=1400&q=80",
            "movie_type": "series",
            "genre": "sci-fi",
            "rating": 8.8,
            "year": 2016,
            "duration": "4 Seasons",
            "views": 8950,
            "featured": True,
        },
        {
            "title": "The Matrix",
            "original_title": "The Matrix",
            "description": "A hacker discovers the truth behind reality.",
            "full_description": "A computer hacker learns the shocking truth that the world he knows is part of an elaborate simulation and joins a rebellion against the machines controlling it.",
            "image_url": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=900&q=80",
            "cover_url": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1400&q=80",
            "movie_type": "movie",
            "genre": "sci-fi",
            "rating": 8.7,
            "year": 1999,
            "duration": "2h 16m",
            "views": 9300,
            "featured": False,
        },
        {
            "title": "The Dark Knight",
            "original_title": "The Dark Knight",
            "description": "Batman faces an enemy that tests Gotham's soul.",
            "full_description": "Under pressure from a city spiraling into chaos, Batman must confront the Joker, a menace who pushes the boundaries of morality and justice in Gotham.",
            "image_url": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=900&q=80",
            "cover_url": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1400&q=80",
            "movie_type": "movie",
            "genre": "action",
            "rating": 9.0,
            "year": 2008,
            "duration": "2h 32m",
            "views": 11000,
            "featured": True,
        },
    ]

    for entry in sample_movies:
        db.add(Movie(**entry))

    db.commit()
