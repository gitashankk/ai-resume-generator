import streamlit as st

st.title("AI Resume & Cover Letter Generator")
st.write("Fill in your details below:")

# Step 1: Choose a template
template = st.selectbox(
    "Choose a Resume Template",
    ["Classic", "Modern", "Creative"]
)

# Input fields
name = st.text_input("Full Name")
email = st.text_input("Email")
summary = st.text_area("Professional Summary / Objective")
skills = st.text_area("Skills")
education = st.text_area("Education (Degree, College, Year)")
experience = st.text_area("Work Experience")

# Optional: choose color and graphic for Modern/Creative templates
if template in ["Modern", "Creative"]:
    header_color = st.color_picker("Pick header color", "#000000")
    graphic = st.selectbox("Choose a graphic/icon", ["📌", "⭐", "💼"])

# Generate resume button
if st.button("Generate Resume"):
    st.success("Resume Generated Successfully!")

    st.markdown("### Resume Preview")

    # Apply formatting based on template
    if template == "Classic":
        st.markdown(f"**Name:** {name}")
        st.markdown(f"**Email:** {email}")
        st.markdown(f"**Professional Summary:** {summary}")
        st.markdown(f"**Skills:** {skills}")
        st.markdown(f"**Education:** {education}")
        st.markdown(f"**Experience:** {experience}")

    elif template == "Modern":
        st.markdown(f"<p style='color:{header_color}; font-weight:bold'>Name: {name}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:{header_color}'>Email: {email}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:{header_color}'>Professional Summary: {summary}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:{header_color}'>Skills: {skills}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:{header_color}'>Education: {education}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:{header_color}'>Experience: {experience}</p>", unsafe_allow_html=True)

    elif template == "Creative":
        st.markdown(f"<p style='color:{header_color}; font-size:18px'>{graphic} Name: {name}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:{header_color}'>{graphic} Email: {email}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:{header_color}'>{graphic} Professional Summary: {summary}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:{header_color}'>{graphic} Skills: {skills}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:{header_color}'>{graphic} Education: {education}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:{header_color}'>{graphic} Experience: {experience}</p>", unsafe_allow_html=True)
