import streamlit as st

st.title("AI Resume & Cover Letter Generator")
st.write("Fill in your details below:")

# Input fields
name = st.text_input("Full Name")
email = st.text_input("Email")
summary = st.text_area("Professional Summary / Objective")  # new line
skills = st.text_area("Skills")
education = st.text_area("Education (Degree, College, Year)")
experience = st.text_area("Work Experience")

# Generate resume button
if st.button("Generate Resume"):
    st.success("Resume Generated Successfully!")

    # Resume Preview with professional formatting
    st.markdown("### Resume Preview")
    st.markdown(f"**Name:** {name}")
    st.markdown(f"**Email:** {email}")
    st.markdown(f"**Professional Summary:** {summary}")  # new line
    st.markdown(f"**Skills:** {skills}")
    st.markdown(f"**Education:** {education}")
    st.markdown(f"**Experience:** {experience}")
