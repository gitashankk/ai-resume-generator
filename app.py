import streamlit as st

st.set_page_config(page_title="AI Resume Generator", layout="centered")

st.title("AI Resume Generator")

# Initialize Session State
if "generated" not in st.session_state:
    st.session_state.generated = False

# Input Section
st.header("Enter Your Details")

name = st.text_input("Full Name")
email = st.text_input("Email Address")
summary = st.text_area("Professional Summary")
skills = st.text_area("Skills (separate with commas)")
education = st.text_area("Education")
experience = st.text_area("Work Experience")

# Template Selection
st.header("Choose Template")
template = st.selectbox("Select Resume Style", ["Classic", "Modern"])

# Generate Button
if st.button("Generate Resume"):
    st.session_state.generated = True
    st.success("Resume Generated Successfully!")

# Resume Preview
if st.session_state.generated:

    st.divider()
    st.header("Resume Preview")

    if template == "Classic":

        st.subheader(name)
        st.write(email)

        st.markdown("### Professional Summary")
        st.write(summary)

        st.markdown("### Skills")
        st.write(skills)

        st.markdown("### Education")
        st.write(education)

        st.markdown("### Experience")
        st.write(experience)

    elif template == "Modern":

        st.markdown(f"""
        <div style="background-color:#f4f6f8;padding:20px;border-radius:10px">
            <h1 style="color:#1f4e79;">{name}</h1>
            <p><strong>{email}</strong></p>
            <hr>
            <h3 style="color:#1f4e79;">Professional Summary</h3>
            <p>{summary}</p>
            <h3 style="color:#1f4e79;">Skills</h3>
            <p>{skills}</p>
            <h3 style="color:#1f4e79;">Education</h3>
            <p>{education}</p>
            <h3 style="color:#1f4e79;">Experience</h3>
            <p>{experience}</p>
        </div>
        """, unsafe_allow_html=True)
