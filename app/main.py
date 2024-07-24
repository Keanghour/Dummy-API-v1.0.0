from fastapi import FastAPI
from app.db.database import init_db
from app.api.v1.routers import router as v1_router

app = FastAPI()

# Initialize database
init_db()

# Include routers
app.include_router(v1_router, prefix="/api/v1")