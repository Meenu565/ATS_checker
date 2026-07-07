from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, jobs, resumes, scoring, threshold, company_analysis, dashboard, reports, settings, candidates
from app.db.base import Base
from app.db.session import engine
import app.db.models # Ensure models are registered

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI ATS Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
app.include_router(resumes.router, tags=["resumes"])
app.include_router(scoring.router, tags=["scoring"])
app.include_router(threshold.router, tags=["threshold"])
app.include_router(company_analysis.router, tags=["company_analysis"])
app.include_router(dashboard.router, tags=["dashboard"])
app.include_router(reports.router, tags=["reports"])
app.include_router(settings.router, tags=["settings"])
app.include_router(candidates.router, tags=["candidates"])

@app.get("/health")
async def health_check():
    return {"status": "ok", "db": "pending", "redis": "pending", "storage": "pending"}
