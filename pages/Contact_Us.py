import streamlit as st
import pandas
from send_email import send_email


df = pandas.read_csv("topics.csv")

with st.form(key="contact_us"):
    user_email = st.text_input("Your Email Address")
    topic = st.selectbox("What topic do you want to discuss?", options=df)
    raw_message = st.text_area("Text")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {topic}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")
