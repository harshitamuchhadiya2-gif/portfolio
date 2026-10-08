"""
Flask Portfolio & Career Intelligence Server
Harshita Muchhadiya - Python Developer & Full-Stack Engineer
"""

import os
import re
import math
from collections import Counter
from flask import Flask, render_template, request, jsonify, send_from_directory, send_file

app = Flask(__name__, template_folder='templates', static_folder='static')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

GH = "https://github.com/harshitamuchhadiya2-gif"
LINKEDIN = "https://www.linkedin.com/in/harshita-muchhadiya-8482b33b4/"

PROFILE_DATA = {
    "name": "Harshita Muchhadiya",
    "title": "Python Developer | Full-Stack Engineer | Machine Learning Enthusiast",
    "email": "harshitamuchhadiya2@gmail.com",
    "phone": "+91 8380444758",
    "location": "Ahmedabad, Gujarat, India",
    "github": GH,
    "github_username": "harshitamuchhadiya2-gif",
    "linkedin": LINKEDIN,
    "live_project": "https://finsight-analytics-five.vercel.app/",
    "bio": (
        "Dedicated and solution-oriented software engineer with practical internship experience "
        "in Python, Django, Flask, React, and Machine Learning. Proven track record of developing "
        "and deploying production applications—including FinSight Analytics and ResumeX AI. "
        "Currently pursuing M.Sc. IT (Business Intelligence & Analytics) at JG University."
    ),
    "education": [
        {"degree": "M.Sc. IT — Business Intelligence & Analytics (BIA)", "school": "JG University", "status": "Pursuing"},
        {"degree": "Bachelor of Computer Applications (BCA)", "school": "Shreyarth University", "status": "Completed"},
        {"degree": "Higher Secondary Certificate (HSC)", "school": "Vikas Gruh School", "status": "2023"},
        {"degree": "Secondary School Certificate (SSC)", "school": "Vikas Gruh School", "status": "2021"}
    ],
    "stats": [
        {"label": "Production Projects", "value": "2 Production"},
        {"label": "Tech Internships", "value": "2"},
        {"label": "Live Deployments", "value": "2 Live"},
        {"label": "Core Technologies", "value": "10+"}
    ]
}

PROJECTS = [
    {
        "id": "finsight-analytics",
        "title": "FinSight Analytics — Corporate Financial Advisory Platform",
        "subtitle": "Live Cloud Deployed Financial Intelligence & Executive Reporting Platform",
        "category": "Full-Stack & Cloud",
        "badge": "Live Production",
        "featured": True,
        "live_url": "https://finsight-analytics-five.vercel.app/",
        "api_docs_url": "https://finsight-api-prod.onrender.com/docs",
        "github_url": GH + "/finsight-analytics",
        "description": (
            "Enterprise financial intelligence and automated advisory platform. Ingests corporate "
            "financial records, computes revenue velocity, EBITDA margin buffers, expense driver "
            "concentrations, and generates Big-4 caliber executive advisory dossiers. Deployed with "
            "React frontend on Vercel and FastAPI backend on Render with MongoDB Atlas."
        ),
        "stack": ["FastAPI", "React 18", "MongoDB Atlas", "Vercel", "Render", "Pandas", "Tailwind CSS"],
        "metrics": [
            "Sub-50ms API response time with production MongoDB Atlas clustering",
            "Interactive financial decision model with client and admin portals",
            "Automated PDF executive advisory report generation engine"
        ]
    },
    {
        "id": "resumex-pro",
        "title": "ResumeX Pro — AI Resume Intelligence & ATS Analyzer",
        "subtitle": "Live AI Career Intelligence & ATS Scoring Web Application",
        "category": "AI / Machine Learning & Full-Stack",
        "badge": "Live Web App",
        "featured": True,
        "live_url": "https://resumex-ai.onrender.com",
        "github_url": GH + "/ResumeX-AI",
        "description": (
            "Production-grade AI resume intelligence platform featuring automated PDF text parsing, "
            "Scikit-Learn TF-IDF vectorization, Cosine Similarity matching, dynamic Chart.js skill gap "
            "visualization, and downloadable ATS evaluation reports."
        ),
        "stack": ["Python", "Flask", "Scikit-Learn", "NLP / TF-IDF", "Chart.js", "Render"],
        "metrics": [
            "95%+ skill identification precision across 250+ tech competencies",
            "Instant cosine similarity scoring with weighted keyword matching",
            "Full-stack web application with downloadable assessment reports"
        ]
    }
]

SKILLS = {
    "Programming Languages": [
        {"name": "Python", "level": 92},
        {"name": "JavaScript (ES6+)", "level": 85},
        {"name": "SQL", "level": 88},
        {"name": "HTML5 & CSS3", "level": 90},
        {"name": "PHP", "level": 80}
    ],
    "Frameworks & Libraries": [
        {"name": "FastAPI", "level": 88},
        {"name": "Flask", "level": 88},
        {"name": "Django", "level": 85},
        {"name": "React.js", "level": 82},
        {"name": "Tailwind CSS & Bootstrap", "level": 88}
    ],
    "AI & Machine Learning": [
        {"name": "Natural Language Processing (NLP)", "level": 82},
        {"name": "TF-IDF & Cosine Similarity", "level": 85},
        {"name": "Scikit-Learn", "level": 80},
        {"name": "Pandas & NumPy", "level": 84},
        {"name": "Data Cleaning", "level": 85}
    ],
    "Databases & Cloud": [
        {"name": "MongoDB Atlas", "level": 88},
        {"name": "Render & Vercel", "level": 88},
        {"name": "MySQL & SQLite", "level": 84},
        {"name": "Git & GitHub", "level": 90},
        {"name": "Docker & Postman", "level": 80}
    ]
}

TECH_KEYWORDS = {
    "python", "flask", "django", "fastapi", "react", "javascript", "html", "css", "sql", "mysql",
    "sqlite", "machine learning", "nlp", "natural language processing", "rest api", "api",
    "git", "github", "tailwind", "pandas", "numpy", "scikit-learn", "data analysis", "docker",
    "mongodb", "atlas", "postman"
}

def extract_keywords(text):
    text_lower = text.lower()
    found = set()
    for kw in TECH_KEYWORDS:
        pattern = r'\b' + re.escape(kw) + r'\b'
        if re.search(pattern, text_lower):
            found.add(kw)
    return found

def compute_similarity(text1, text2):
    def tokenize(t):
        return re.findall(r'\b[a-zA-Z]{2,}\b', t.lower())

    tokens1 = tokenize(text1)
    tokens2 = tokenize(text2)
    if not tokens1 or not tokens2:
        return 0.0

    tf1 = Counter(tokens1)
    tf2 = Counter(tokens2)

    all_words = set(tf1.keys()).union(set(tf2.keys()))
    dot_product = sum(tf1[w] * tf2[w] for w in all_words)
    mag1 = math.sqrt(sum(v * v for v in tf1.values()))
    mag2 = math.sqrt(sum(v * v for v in tf2.values()))

    if mag1 == 0 or mag2 == 0:
        return 0.0
    return round((dot_product / (mag1 * mag2)) * 100, 1)

# Routes
@app.route("/")
def home():
    return render_template("index.html", profile=PROFILE_DATA, projects=PROJECTS, skills=SKILLS)

@app.route("/resume")
def resume():
    return render_template("resume.html", profile=PROFILE_DATA, projects=PROJECTS, skills=SKILLS)

@app.route("/download/resume")
@app.route("/resume.pdf")
def download_resume():
    static_pdf = os.path.join(BASE_DIR, "static", "Harshita_Muchhadiya_Resume.pdf")
    if os.path.exists(static_pdf):
        return send_file(static_pdf, as_attachment=True, download_name="Harshita_Muchhadiya_Resume.pdf")
    return send_from_directory("templates", "resume.html", as_attachment=True)

@app.route("/preview")
def preview():
    return render_template("preview.html", profile=PROFILE_DATA, projects=PROJECTS, skills=SKILLS)

@app.route("/api/profile")
def api_profile():
    return jsonify(PROFILE_DATA)

@app.route("/api/projects")
def api_projects():
    return jsonify(PROJECTS)

@app.route("/api/skills")
def api_skills():
    return jsonify(SKILLS)

@app.route("/api/analyze-resume", methods=["POST"])
def api_analyze_resume():
    data = request.get_json() or {}
    resume_text = data.get("resume", "").strip()
    job_desc = data.get("job_description", "").strip()

    if not resume_text:
        return jsonify({"error": "Resume text is required"}), 400
    if not job_desc:
        job_desc = "Seeking a Python Developer with experience in Flask, FastAPI, Django, React, REST APIs, and MySQL/MongoDB."

    resume_skills = extract_keywords(resume_text)
    job_skills = extract_keywords(job_desc)

    matching_skills = resume_skills.intersection(job_skills)
    missing_skills = job_skills.difference(resume_skills)

    skill_match_ratio = (len(matching_skills) / len(job_skills) * 100) if job_skills else 80.0
    cosine_sim = compute_similarity(resume_text, job_desc)
    overall_score = min(100, round(0.6 * skill_match_ratio + 0.4 * min(100, cosine_sim * 1.8), 1))

    recommendations = []
    if missing_skills:
        recommendations.append(f"Consider highlighting experience with: {', '.join(sorted(list(missing_skills)[:5]))}")
    if len(resume_skills) < 5:
        recommendations.append("Add more specific technical tooling and framework names in your project descriptions.")
    if not recommendations:
        recommendations.append("Strong technical alignment with the target job profile! Ready for interview discussion.")

    return jsonify({
        "overall_score": overall_score,
        "skill_match_ratio": round(skill_match_ratio, 1),
        "cosine_similarity": cosine_sim,
        "resume_skills": sorted(list(resume_skills)),
        "target_skills": sorted(list(job_skills)),
        "matching_skills": sorted(list(matching_skills)),
        "missing_skills": sorted(list(missing_skills)),
        "recommendations": recommendations
    })

@app.route("/api/contact", methods=["POST"])
def api_contact():
    data = request.get_json() or {}
    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    message = data.get("message", "").strip()

    if not name or not email or not message:
        return jsonify({"success": False, "error": "All fields are required"}), 400

    return jsonify({
        "success": True,
        "message": f"Thank you {name}! Your message has been received. Harshita will respond to {email} shortly."
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting portfolio server on port {port}...")
    app.run(host="0.0.0.0", port=port, debug=True)
