import streamlit as st

st.title("AI Resume & Cover Letter Generator")
st.write("Fill in your details below:")

# Input fields
name = st.text_input("Full Name")                             # line 4
email = st.text_input("Email")                                # line 5
skills = st.text_area("Skills")                               # line 6
education = st.text_area("Education (Degree, College, Year)") # line 7
experience = st.text_area("Work Experience")                 # line 8

# Generate resume button
if st.button("Generate Resume"):
    st.success("Resume Generated Successfully!")

    # Resume Preview with professional formatting
    st.markdown("### Resume Preview")
    st.markdown(f"**Name:** {name}")
    st.markdown(f"**Email:** {email}")
    st.markdown(f"**Skills:** {skills}")
    st.markdown(f"**Education:** {education}")
    st.markdown(f"**Experience:** {experience}")
