# 💼 Skill Trend Detector – Job Market Analysis System

This project is a complete **Job Market Analysis System** that analyzes job descriptions to extract skill patterns, detect trends, and visualize insights in the job market. It was developed as part of the AI/ML Junior Developer assignment by CultureMonkey.

---

## 🚀 Project Features

### ✅ Part 1: Data Analysis
- Extracted and compared technical skills across Entry-level and Senior roles.
- Identified the Top 3 in-demand skills.
- Found patterns such as rare, senior-only technical skills.

### 📊 Part 2: Data Visualization
- Visualized:
  - Skill distribution by seniority.
  - Top 10 most in-demand skills.
  - Geographic job distribution (if location data available).
  - Salary patterns by seniority level.

### 🧠 Part 3: Skill Trend Detector
- Extracted skills from job descriptions.
- Categorized skills as **emerging** or **established** based on usage frequency.
- Calculated a normalized **trend score** for each skill.

### 🌐 Part 4: REST API Deployment
- Developed a FastAPI-based REST service.
- Accepts job descriptions and returns detected skills with categories and trend scores.
- Built-in Swagger documentation for testing and demonstration.

---

## ⚙️ Tech Stack

- Python 3.10+
- pandas, matplotlib, seaborn
- FastAPI
- Uvicorn
- wordcloud, nltk, re, collections

---

## 📂 Project Structure

