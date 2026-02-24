import streamlit as st

# --- App Config ---
st.set_page_config(page_title="AI Resume Builder", layout="wide")
st.title("AI Resume Builder")
st.write("Create a professional, modern resume in minutes.")

# --- Sidebar Inputs ---
st.sidebar.header("Enter Your Details")

# Personal Info
name = st.sidebar.text_input("Full Name", "Gita Shanker")
email = st.sidebar.text_input("Email", "Gitas_1288@yahoo.com")
phone = st.sidebar.text_input("Phone", "123-456-7890")
city = st.sidebar.text_input("City", "Metuchen, NJ")

# Template Choice
template = st.sidebar.selectbox("Choose Resume Template", ["Classic", "Modern"])

# Professional Summary
st.sidebar.subheader("Professional Summary")
summary = st.sidebar.text_area(
    "Summary", 
    "Motivated and detail-oriented professional with a background in Computer and Information Systems and HR. Eager to contribute and grow in a professional role."
)

# Skills
st.sidebar.subheader("Skills (comma-separated)")
skills = st.sidebar.text_area(
    "Skills", 
    "Java, OOP, HTML, CSS, JavaScript, SQL, MS Word, Excel, Outlook, Problem-solving, Teamwork, Communication, Time Management"
)

# Education
st.sidebar.subheader("Education")
degree1 = st.sidebar.text_input("Degree 1", "Bachelor of Arts and Sciences")
school1 = st.sidebar.text_input("School 1", "Rutgers University")
year1 = st.sidebar.text_input("Year 1", "2024")

degree2 = st.sidebar.text_input("Degree 2", "Associate Degree in Computer and Information Systems")
school2 = st.sidebar.text_input("School 2", "Middlesex College")
year2 = st.sidebar.text_input("Year 2", "2022")

# Work Experience
st.sidebar.subheader("Work Experience")
job_title = st.sidebar.text_input("Job Title", "Home-Based Business Owner")
company = st.sidebar.text_input("Company", "Self-Managed")
duration = st.sidebar.text_input("Duration", "Start Year – Present")
responsibilities = st.sidebar.text_area(
    "Responsibilities",
    "Managed client communications, service delivery, and daily operations. Streamlined workflows and maintained financial records."
)

# --- Generate Resume ---
if st.sidebar.button("Generate Resume"):
    if template == "Modern":
        # --- Modern: Two columns ---
        col1, col2 = st.columns([2, 1])
        with col1:
            st.header(f"{name}")
            st.subheader("Professional Summary")
            st.write(summary)
            st.subheader("Work Experience")
            st.markdown(f"**{job_title}** – {company} | {duration}")
            st.write(responsibilities)
            st.subheader("Education")
            st.markdown(f"**{degree1}** – {school1}, {year1}")
            st.markdown(f"**{degree2}** – {school2}, {year2}")
        with col2:
            st.subheader("Contact Info")
            st.write(f"📧 {email}")
            st.write(f"📞 {phone}")
            st.write(f"📍 {city}")
            st.subheader("Skills")
            st.write(" • ".join([skill.strip() for skill in skills.split(",")]))
    else:  # Classic template
        st.header(f"{name}")
        st.subheader("Contact Info")
        st.write(f"📧 {email}  |  📞 {phone}  |  📍 {city}")
        st.subheader("Professional Summary")
        st.write(summary)
        st.subheader("Work Experience")
        st.markdown(f"**{job_title}** – {company} | {duration}")
        st.write(responsibilities)
        st.subheader("Education")
        st.markdown(f"**{degree1}** – {school1}, {year1}")
        st.markdown(f"**{degree2}** – {school2}, {year2}")
        st.subheader("Skills")
        st.write(" • ".join([skill.strip() for skill in skills.split(",")]))
