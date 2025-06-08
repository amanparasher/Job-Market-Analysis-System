
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import pandas as pd

from trend_finder_model import skill_trend_detector, extract_skills_from_description, get_skill_frequencies

app = FastAPI(title="Skill Trend Detector API", version="1.0.0")

# Load dataset and build frequency dict once
try:
    df = pd.read_csv("dataset.csv")
    df['job_description_text'] = df['job_description_text'].fillna("")
    df['extracted_skills'] = df['job_description_text'].apply(extract_skills_from_description)
    skill_freq_dict = get_skill_frequencies(df['extracted_skills'].tolist())
    print(f"Loaded {len(skill_freq_dict)} skills from dataset")
except Exception as e:
    print(f"Error loading dataset: {e}")
    # Fallback to sample data if dataset fails to load
    skill_freq_dict = {
        'python': 95, 'sql': 87, 'java': 78, 'tensorflow': 45, 'pytorch': 38,
        'machine learning': 82, 'deep learning': 34, 'aws': 56, 'azure': 41,
        'tableau': 29, 'power bi': 22, 'scikit-learn': 31, 'diffusion models': 8
    }

# Request and Response Schemas
class JobDescription(BaseModel):
    job_description: str

class SkillEntry(BaseModel):
    skill: str
    category: str
    trend_score: float

class SkillResponse(BaseModel):
    detected_skills: List[SkillEntry]

# Root endpoint
@app.get("/")
def read_root():
    return {
        "message": "Skill Trend Detector API",
        "version": "1.0.0",
        "docs": "/docs"
    }

# Health check
@app.get("/health")
def health_check():
    return {"status": "healthy", "total_skills": len(skill_freq_dict)}

# Main endpoint
@app.post("/detect_skills", response_model=SkillResponse)
def detect_skills_endpoint(payload: JobDescription):
    if not payload.job_description.strip():
        raise HTTPException(status_code=400, detail="Job description is empty.")
    
    try:
        result = skill_trend_detector(payload.job_description, skill_freq_dict)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)