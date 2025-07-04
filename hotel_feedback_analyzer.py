import streamlit as st
from transformers import pipeline

# Load sentiment analysis model from Hugging Face
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

analyzer = load_model()

# Streamlit UI
st.set_page_config(page_title="Hotel Feedback Analyzer (HF)", layout="centered")
st.title("\U0001F3E8 Hotel Feedback Analyzer (Hugging Face)")

review = st.text_area("Enter a hotel review:")

if st.button("Analyze Review"):
    if review:
        result = analyzer(review)[0]
        sentiment = result["label"]

        # Simple topic guess
        topics = []
        review_lower = review.lower()
        if "food" in review_lower: topics.append("Food")
        if "room" in review_lower or "bathroom" in review_lower: topics.append("Rooms")
        if "staff" in review_lower: topics.append("Staff")
        if "clean" in review_lower or "dirty" in review_lower: topics.append("Cleanliness")
        if "location" in review_lower: topics.append("Location")

        st.subheader("\U0001F50D Analysis Result:")
        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Topics:** {', '.join(topics) if topics else 'General'}")
    else:
        st.warning("Please enter a review before clicking Analyze.")
