# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import pandas as pd

from trend_finder_model import skill_trend_detector, extract_skills_from_description, get_skill_frequencies

app = FastAPI(title="Skill Trend Detector API")

# Load dataset and build frequency dict once
df = pd.read_csv("dataset.csv")
df['job_description_text'] = df['job_description_text'].fillna("")
df['extracted_skills'] = df['job_description_text'].apply(extract_skills_from_description)

skill_freq_dict = get_skill_frequencies(df['extracted_skills'].tolist())

# Request and Response Schemas
class JobDescription(BaseModel):
    job_description: str

class SkillEntry(BaseModel):
    skill: str
    category: str
    trend_score: float

class SkillResponse(BaseModel):
    detected_skills: List[SkillEntry]

# Endpoint
@app.post("/detect_skills", response_model=SkillResponse)
def detect_skills_endpoint(payload: JobDescription):
    if not payload.job_description.strip():
        raise HTTPException(status_code=400, detail="Job description is empty.")
    
    result = skill_trend_detector(payload.job_description, skill_freq_dict)
    return result
