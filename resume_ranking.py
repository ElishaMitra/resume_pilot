import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from PIL import Image
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Predefined list of skills
SKILL_LIST = [
    "Python", "Java", "JavaScript", "C++", "SQL", "Machine Learning", "Deep Learning",
    "Data Science", "React", "Node.js", "AWS", "Docker", "Kubernetes", "Flask",
    "Django", "TensorFlow", "Keras", "Pandas", "NumPy", "Data Structures", "Algorithms"
]

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text.strip()

# Function to extract skills from text
def extract_skills(text):
    found_skills = set()
    for skill in SKILL_LIST:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text, re.IGNORECASE):
            found_skills.add(skill)
    return found_skills

# Function to rank resumes based on job description
def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()

    # Calculate cosine similarity
    job_description_vector = vectors[0]
    resume_vectors = vectors[1:]
    cosine_similarities = cosine_similarity([job_description_vector], resume_vectors).flatten()
    
    return cosine_similarities

# Streamlit app
st.set_page_config(
    page_title="Resume Pilot",
    page_icon='./Logo/logo.png',
)



st.markdown(
    "<h1 style='color:rgb(28, 30, 167); font-family: Algerian, sans-serif; font-weight: bold;'>🛩️ Resume Pilot</h1>", 
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='color:rgb(0, 170, 255); font-style: italic;'>AI Resume Screening & Candidate Ranking System</h3>", 
    unsafe_allow_html=True
)

img = Image.open('./Logo/Image1.png')
img = img.resize((650, 350))
st.image(img)

# Job description input
st.header("Job Description")
job_description = st.text_area("Enter the job description")

# File uploader
st.header("Upload Resumes")
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files and job_description:
    st.header("Ranking Resumes")
    
    resumes = []
    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        resumes.append(text)

    # Rank resumes
    scores = rank_resumes(job_description, resumes)

    # Extract skills from job description and resumes
    job_skills = extract_skills(job_description)
    resume_skills = set()
    for resume_text in resumes:
        resume_skills.update(extract_skills(resume_text))

    missing_skills = job_skills - resume_skills  # Find missing skills

    # Display scores
    results = pd.DataFrame({"Resume": [file.name for file in uploaded_files], "Score": scores})
    results = results.sort_values(by="Score", ascending=False)

    st.write(results)

    # Display extracted skills
    st.header("🔍 Skills Analysis")
    st.write(f"**Skills Required for the Job:** {', '.join(job_skills) if job_skills else 'No specific skills detected.'}")
    st.write(f"**Skills Found in Resumes:** {', '.join(resume_skills) if resume_skills else 'No relevant skills detected.'}")

    # Display missing skills
    if missing_skills:
        st.warning(f"⚠️ Your resumes are missing these important skills: {', '.join(missing_skills)}")
    else:
        st.success("✅ Your resumes contain all the required skills!")


