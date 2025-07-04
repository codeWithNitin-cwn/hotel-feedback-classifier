import streamlit as st
from transformers import pipeline

# Load sentiment model
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

analyzer = load_model()

# Page config
st.set_page_config(page_title="Nitin's Hotel Feedback Analyzer", layout="centered")

# Enhanced Styling
st.markdown("""
    <style>
    body {
        background-color: #f2f6fc;
    }
    .header {
        text-align: center;
        font-size: 40px;
        font-weight: 900;
        color: #4a90e2;
        padding-top: 20px;
    }
    .subtext {
        text-align: center;
        font-size: 20px;
        color: #6e6e6e;
        margin-bottom: 30px;
    }
    .card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        margin-top: 25px;
        font-size: 18px;
        color: #333;
        line-height: 1.6;
    }
    .card h4 {
        color: #28a745;
        margin-bottom: 15px;
    }
    .card code {
        background-color: #e7f3ff;
        color: #2c3e50;
        padding: 3px 8px;
        border-radius: 6px;
        font-size: 16px;
    }
    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #ced4da;
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
    }
    .stButton>button {
        background-color: #4a90e2;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.6em 1.2em;
        border: none;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #357ABD;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='header'>🏨 Nitin's Hotel Feedback Analyzer</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Smart AI insights on hotel reviews — completely free & stylish!</div>", unsafe_allow_html=True)

# Input field
review = st.text_area("✍️ Enter your hotel feedback below:", height=150)

# Analyze Button
if st.button("🧠 Analyze Feedback"):
    if review:
        result = analyzer(review)[0]
        sentiment = result["label"]

        # Basic Topic Detection
        topics = []
        text = review.lower()
        if "food" in text: topics.append("Food")
        if "room" in text or "bathroom" in text: topics.append("Rooms")
        if "staff" in text: topics.append("Staff")
        if "clean" in text or "dirty" in text: topics.append("Cleanliness")
        if "location" in text: topics.append("Location")

        # Result Card
        st.markdown("""
            <div class='card'>
                <h4>✅ Thank you for your feedback, Nitin!</h4>
                <p><strong>🧾 Sentiment:</strong> <code>{}</code></p>
                <p><strong>🔍 Topics:</strong> <code>{}</code></p>
            </div>
        """.format(sentiment, ', '.join(topics) if topics else 'General'), unsafe_allow_html=True)
    else:
        st.warning("Please enter a review to analyze.")
