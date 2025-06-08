# trend_model.py

import re
from collections import Counter

# Sample skill list — you can extend this
skill_keywords = [
    'python', 'r', 'sql', 'java', 'c++', 'pytorch', 'tensorflow', 'excel',
    'machine learning', 'deep learning', 'nlp', 'hadoop', 'spark', 'tableau',
    'power bi', 'scikit-learn', 'keras', 'aws', 'azure', 'gcp', 'flask', 'fastapi',
    'diffusion models'
]

def clean_data(text: str) -> str:
    text = text.lower()
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def extract_skills_from_description(text: str) -> list:
    cleaned = clean_data(text)
    return [skill for skill in skill_keywords if skill in cleaned]

def get_skill_frequencies(skill_lists: list) -> Counter:
    all_skills = [skill for sublist in skill_lists for skill in sublist]
    return Counter(all_skills)

def classify_skill(skill: str, freq_dict: dict, max_freq: int, threshold: int = 3):
    freq = freq_dict.get(skill, 0)
    trend_score = round(freq / max_freq, 2)
    category = "emerging" if freq < threshold else "established"
    return category, trend_score

def skill_trend_detector(description: str, freq_dict: dict) -> dict:
    max_freq = max(freq_dict.values()) if freq_dict else 1
    skills = extract_skills_from_description(description)
    result = []

    for skill in skills:
        category, score = classify_skill(skill, freq_dict, max_freq)
        result.append({
            "skill": skill,
            "category": category,
            "trend_score": score
        })

    return {"detected_skills": result}
