import streamlit as st
from textblob import TextBlob

# App title
st.title("Sentiment Analysis App")

# User input text
user_input = st.text_area("Enter Text to Analyze", "Type your text here...")

# Analyze button
if st.button("Analyze Sentiment"):
    # Analyze the sentiment
    blob = TextBlob(user_input)
    sentiment = blob.sentiment

    # Display sentiment results
    st.subheader("Sentiment Analysis Results")
    st.write(f"**Polarity:** {sentiment.polarity} (Range: -1 to 1)")
    st.write(f"**Subjectivity:** {sentiment.subjectivity} (Range: 0 to 1)")

    # Sentiment interpretation
    if sentiment.polarity > 0:
        st.success("The sentiment is Positive 😊")
    elif sentiment.polarity < 0:
        st.error("The sentiment is Negative 😞")
    else:
        st.info("The sentiment is Neutral 😐")
