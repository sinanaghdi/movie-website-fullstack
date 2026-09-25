from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager

from .database import Base, SessionLocal, engine
from .crud import seed_movies, seed_admin_user
from .routes import auth, admin, movies, pages


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_movies(db)
        seed_admin_user(db)
    finally:
        db.close()
    yield
    # Shutdown


app = FastAPI(
    title="Flakes Movie Platform",
    description="Multi-page movie streaming platform",
    version="2.0.0",
    lifespan=lifespan
)

# Mount static files
try:
    app.mount("/css", StaticFiles(directory="css"), name="css")
    app.mount("/js", StaticFiles(directory="js"), name="js")
    app.mount("/img", StaticFiles(directory="img"), name="img")
except Exception:
    pass

# Setup templates
templates = Jinja2Templates(directory="templates")

# Include routes
app.include_router(pages.router)
app.include_router(auth.router)
app.include_router(movies.router, prefix="/api")
app.include_router(admin.router, prefix="/api")
