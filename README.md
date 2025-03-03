•Resume Pilot – AI Resume Screening & Candidate Ranking System
----------------------------------------------------------------
This project is an AI-powered resume screening and ranking system built using Streamlit, scikit-learn, and PyPDF2. It allows users to upload resumes in PDF format, compare them against a given job description, and rank them based on TF-IDF & Cosine Similarity. Additionally, it extracts skills from resumes and highlights missing skills required for the job.

🚀 Features
--------------------
✅ Upload multiple PDF resumes.
✅ Enter a job description for comparison.
✅ Uses TF-IDF & Cosine Similarity for ranking.
✅ Extracts technical skills from resumes and job descriptions.
✅ Identifies missing skills in resumes.
✅ Displays ranked resumes with similarity scores.

How It Works
---------------------
🔹 Upload PDF resumes using the file uploader.
🔹 Enter a job description in the provided text area.
🔹 Extracts text from resumes and converts them into TF-IDF vectors.
🔹 Compares job description & resumes using cosine similarity.
🔹 Ranks resumes based on relevance.
🔹 Extracts & highlights skills from resumes.
🔹 Identifies missing skills required for the job.

Requirements
---------------
streamlit
PyPDF2
pandas
scikit-learn
numpy
PIL (Pillow)

Install using:
-----------------
pip install -r requirements.txt  

Folder Structure
----------------------
resume_pilot/  
│── .venv/  
│── resume_ranking.py  
│── requirements.txt 
│── resume_ranking.ipynb   
│── Sample/  
│   ├── sample_resume.pdf  
│── Logo/  
│   ├── logo.png  
│   ├── Image1.png  
│── README.md  
│── .gitignore  

Run the Application
----------------------------

streamlit run resume_ranking.py  

Deployment
------------------
Deploy on Streamlit Cloud (Free)
1️⃣ Push your project to GitHub.
2️⃣ Go to Streamlit Cloud and log in.
3️⃣ Click New App, select your GitHub repo, and set the file path to app.py.
4️⃣ Click Deploy 🚀

End Users
-----------------
🔹 HR & Recruiters – Automates resume screening for faster hiring.
🔹 Hiring Managers – Ranks resumes efficiently for job roles.
🔹 Job Portals – Enhances resume-job matching accuracy.
🔹 AI Enthusiasts & Students – Learn NLP-based resume analysis.

🔮 Future Scope
-------------------------
✅ AI-Based Scoring – Use ML/Deep Learning for better ranking.
✅ Advanced NLP – Integrate BERT/GPT for deeper analysis.
✅ Multi-Format Support – Add DOCX, TXT & OCR for image-based resumes.
✅ Skill Matching – Automatically extract skills & experience.
✅ API Integration – Connect with job portals & HR systems.

◘ Conclusion
---------------------
Resume Pilot streamlines resume screening by automating resume ranking and skill matching. Using TF-IDF and Cosine Similarity, it ensures fast, objective, and accurate candidate shortlisting. With PDF text extraction, real-time ranking, and easy deployment via Streamlit, this project provides a scalable, efficient, and user-friendly solution for recruiters, hiring managers, and job portals. 🚀

