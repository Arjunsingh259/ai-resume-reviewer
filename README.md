# 🧠 AI Resume Reviewer

An intelligent web app that reviews resumes using AI and provides feedback to job seekers or students.

## 🚀 Features

- Upload PDF resumes
- Extracts resume text automatically
- Sends text to an AI model for review
- Displays structured feedback and suggestions
- Powered by OpenRouter API (uses ChatGPT or similar models)

## 💡 How It Works

1. Built using **Python** and **Streamlit**
2. Uses `pdfplumber` to extract resume content
3. Sends content to OpenRouter API for AI-based analysis
4. Presents results on an interactive web interface

## 📂 Project Structure

ai-resume-reviewer/
│
├── .streamlit/
│ └── config.toml
│
├── app.py # Streamlit app logic
├── requirements.txt # Python dependencies
└── README.md # This file

csharp
Copy
Edit

## 🔐 Secrets Management

- API key is **not included** in this repository.
- To use this project, you must create your own `.streamlit/secrets.toml` file:

```toml
[openrouter]
api_key = "your_openrouter_api_key_here"
Add this file manually and keep it secret (never upload to GitHub).

The file is in .gitignore and was completely removed from Git history using BFG.

📦 Installation
Clone the repo:

bash
Copy
Edit
git clone https://github.com/Arjunsingh259/ai-resume-reviewer.git
cd ai-resume-reviewer
Create and activate a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Create .streamlit/secrets.toml and add your key.

Run the app:

bash
Copy
Edit
streamlit run app.py

👤 Author
Arjun Singh


📜 License
This project is open source and free to use.

yaml
Copy
Edit

---

#### 3. **Save the File** in VS Code

---

#### 4. **Add, Commit, and Push to GitHub**

```bash
git add README.md
git commit -m "Add detailed README file"
git pull origin main --rebase
git push origin main