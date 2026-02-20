
import streamlit as st

st.title("AI Resume & Cover Letter Generator")

st.write("Fill in your details below:")

name = st.text_input("Full Name")
email = st.text_input("Email")
skills = st.text_area("Skills")
experience = st.text_area("Work Experience")

if st.button("Generate Resume"):
    st.success("Resume Generated Successfully!")

    st.write("### Resume Preview")
    st.write(f"Name: {name}")
    st.write(f"Email: {email}")
    st.write(f"Skills: {skills}")
    st.write(f"Experience: {experience}")
