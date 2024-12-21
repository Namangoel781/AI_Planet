from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import pdf, qa
from app.core.config import settings
from app.core.events import create_start_app_handler, create_stop_app_handler

app = FastAPI(title="PDF Q&A API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add event handlers
app.add_event_handler("startup", create_start_app_handler(app))
app.add_event_handler("shutdown", create_stop_app_handler(app))

# Include routers
app.include_router(pdf.router, prefix="/api/v1", tags=["pdf"])
app.include_router(qa.router, prefix="/api/v1", tags=["qa"])
