import streamlit as st
import pdfplumber
import requests

st.set_page_config(page_title="AI Resume Reviewer")
st.title("📄 AI Resume Reviewer")

api_key = st.secrets["OPENROUTER_API_KEY"]

# --- PDF Upload ---
uploaded_file = st.file_uploader("📎 Upload your resume (PDF only)", type=["pdf"])
resume_text = ""

if uploaded_file is not None:
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            resume_text += page.extract_text() or ""

    st.success("✅ Resume loaded successfully!")

# --- Text Area (Optional Manual Edit) ---
edited_text = st.text_area("📝 You can also edit the resume text:", resume_text, height=300)

# --- Send to ChatGPT ---
if st.button("✨ Get AI Feedback") and edited_text.strip() != "":
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": f"Review this resume and suggest improvements:\n\n{edited_text}"}
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        st.subheader("🧠 AI Suggestions")
        st.write(reply)
    else:
        st.error("❌ Something went wrong. Try again later.")
