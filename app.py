import streamlit as st

st.set_page_config(page_title="AI Resume Generator", layout="centered")

st.title("AI Resume Generator")

# -----------------------------
# Initialize Session State
# -----------------------------
if "name" not in st.session_state:
    st.session_state.name = ""

if "email" not in st.session_state:
    st.session_state.email = ""

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "skills" not in st.session_state:
    st.session_state.skills = ""

if "education" not in st.session_state:
    st.session_state.education = ""

if "experience" not in st.session_state:
    st.session_state.experience = ""

if "template" not in st.session_state:
    st.session_state.template = "Classic"

if "generated" not in st.session_state:
    st.session_state.generated = False


# -----------------------------
# Resume Input Section
# -----------------------------
st.header("Enter Your Details")

st.session_state.name = st.text_input(
    "Full Name", value=st.session_state.name
)

st.session_state.email = st.text_input(
    "Email Address", value=st.session_state.email
)

st.session_state.summary = st.text_area(
    "Professional Summary", value=st.session_state.summary
)

st.session_state.skills = st.text_area(
    "Skills (separate with commas)", value=st.session_state.skills
)

st.session_state.education = st.text_area(
    "Education", value=st.session_state.education
)

st.session_state.experience = st.text_area(
    "Work Experience", value=st.session_state.experience
)


# -----------------------------
# Template Selection
# -----------------------------
st.header("Choose Template")

st.session_state.template = st.selectbox(
    "Select Resume Style",
    ["Classic", "Modern"],
    index=["Classic", "Modern"].index(st.session_state.template),
)


# -----------------------------
# Generate Button
# -----------------------------
if st.button("Generate Resume"):
    st.session_state.generated = True
    st.success("Resume Generated Successfully!")


# -----------------------------
# Resume Preview Section
# -----------------------------
if st.session_state.generated:

    st.divider()
    st.header("Resume Preview")

    if st.session_state.template == "Classic":

        st.subheader(st.session_state.name)
        st.write(st.session_state.email)

        st.markdown("### Professional Summary")
        st.write(st.session_state.summary)

        st.markdown("### Skills")
        st.write(st.session_state.skills)

        st.markdown("### Education")
        st.write(st.session_state.education)

        st.markdown("### Experience")
        st.write(st.session_state.experience)

    elif st.session_state.template == "Modern":

        st.markdown(
            f"""
            <div style="background-color:#f4f6f8;padding:20px;border-radius:10px">
                <h1 style="color:#1f4e79;">{st.session_state.name}</h1>
                <p><strong>{st.session_state.email}</strong></p>
                <hr>
                <h3 style="color:#1f4e79;">Professional Summary</h3>
                <p>{st.session_state.summary}</p>
                <h3 style="color:#1f4e79;">Skills</h3>
                <p>{st.session_state.skills}</p>
                <h3 style="color:#1f4e79;">Education</h3>
                <p>{st.session_state.education}</p>
                <h3 style="color:#1f4e79;">Experience</h3>
                <p>{st.session_state.experience}</p>
            </div>
            """,
            unsafe_allow_html=True,
