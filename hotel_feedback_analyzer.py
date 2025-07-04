# Hotel Feedback Analyzer Web App using Streamlit + OpenAI

import openai
import pandas as pd
import streamlit as st

# Set your OpenAI API key
openai.api_key = "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"

# Define prompt template
def build_prompt(review):
    return f"""
Read the following hotel review and do two things:
1. Classify the sentiment as Positive, Negative, or Neutral.
2. Extract key topics mentioned (e.g., Food, Staff, Rooms, Cleanliness, Location).

Review: "{review}"

Answer:
Sentiment:
Topics:
"""

# Function to analyze a single review
def analyze_review(review):
    prompt = build_prompt(review)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        content = response.choices[0].message.content.strip()
        parts = content.split("\n")
        sentiment = ""
        topics = ""
        for part in parts:
            if part.lower().startswith("sentiment"):
                sentiment = part.split(":")[-1].strip()
            if part.lower().startswith("topics"):
                topics = part.split(":")[-1].strip()
        return sentiment, topics
    except Exception as e:
        return "Error", str(e)

# Streamlit UI
st.set_page_config(page_title="Hotel Feedback Analyzer", layout="centered")
st.title("🏨 Hotel Feedback Analyzer")

review_input = st.text_area("Enter a hotel review:")

if st.button("Analyze Review"):
    if review_input:
        sentiment, topics = analyze_review(review_input)
        st.subheader("🔍 Analysis Result:")
        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Topics:** {topics}")
    else:
        st.warning("Please enter a review before clicking Analyze.")
