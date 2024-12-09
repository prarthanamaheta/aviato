from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import endpoints

app = FastAPI(title="Aviato Users Management API", docs_url="/docs", redoc_url="/redoc")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(endpoints.router, prefix="/users", tags=["Users"])
app.include_router(endpoints.router, prefix="/docs", tags=["Docs"])
