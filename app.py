import streamlit as st

st.title("AI Resume & Cover Letter Generator")
st.write("Fill in your details below:")

# Input fields
name = st.text_input("Full Name")
email = st.text_input("Email")
summary = st.text_area("Professional Summary / Objective")
skills = st.text_area("Skills")
education = st.text_area("Education (Degree, College, Year)")
experience = st.text_area("Work Experience")

# Initialize template variable
template = "Classic"  # default

st.write("### Choose a Resume Template:")

# Display images as clickable templates
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Classic"):
        template = "Classic"
    st.image("IMG_1706.png", caption="Classic Template Example", use_column_width=True)

with col2:
    if st.button("Modern"):
        template = "Modern"
    st.image("IMG_1719.jpeg", caption="Modern Template Example", use_column_width=True)

with col3:
    if st.button("Creative"):
        template = "Creative"
    st.image("IMG_1720.jpeg", caption="Creative Template Example", use_column_width=True)

# Generate Resume button
if st.button("Generate Resume"):
    st.success("Resume Generated Successfully!")
    st.markdown("### Resume Preview")

    if template == "Classic":
        st.markdown(f"**Name:** {name}")
        st.markdown(f"**Email:** {email}")
        st.markdown(f"**Professional Summary:** {summary}")
        st.markdown(f"**Skills:** {skills}")
        st.markdown(f"**Education:** {education}")
        st.markdown(f"**Experience:** {experience}")

    elif template == "Modern":
        st.markdown(f"<p style='color:blue; font-weight:bold'>Name: {name}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:blue'>Email: {email}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:blue'>Professional Summary: {summary}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:blue'>Skills: {skills}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:blue'>Education: {education}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:blue'>Experience: {experience}</p>", unsafe_allow_html=True)

    elif template == "Creative":
        icon = "💼"
        st.markdown(f"<p style='font-size:18px'>{icon} Name: {name}</p>", unsafe_allow_html=True)
        st.markdown(f"<p>{icon} Email: {email}</p>", unsafe_allow_html=True)
        st.markdown(f"<p>{icon} Professional Summary: {summary}</p>", unsafe_allow_html=True)
        st.markdown(f"<p>{icon} Skills: {skills}</p>", unsafe_allow_html=True)
        st.markdown(f"<p>{icon} Education: {education}</p>", unsafe_allow_html=True)
        st.markdown(f"<p>{icon} Experience: {experience}</p>", unsafe_allow_html=True)
