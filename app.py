from pathlib import Path

import streamlit as st
from PIL import Image

#---Path SEETINGS---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

    


# "🏆 Data Visualization Chart- By Using Python in Jupyter": "https://github.com/smritibharti870/python_projects",
#     }
    
# st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)




# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Smriti Bharti"
PAGE_ICON = ":wave:"
NAME = "Smriti Bharti"
DESCRIPTION = """
Looking to utilize my technical and creative skills in an esteemed organization. Well-versed in MySQL, HTML,Django, HTML, CSS and Python. Tech-savvy, fast learner with innate communication skills and a natural curiosity for different computer languages"""
EMAIL = "smritibharti0711@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/smriti-bharti-69000b13b/",
    "GitHub": "https://github.com/smritibharti870",
}
PROJECTS = {
    "🏆 Employee Management System- By Using HTML, Django and Python": "https://github.com/smritibharti870/Employee-Management-System",
    "🏆 Data Visualization Chart- By using Javascript and HTML": "https://github.com/smritibharti870/Data-Chart-By-Using-JS",
    "🏆 Data Visualization Chart- By Using Python in Jupyter": "https://github.com/smritibharti870/python_projects",
    "🏆 Customer self service system- Key skills used in the project(Java, JDBC, JSON, JPA, Hibernate, Spring-Boot, Angular/s, Spring MVC, SQL, Oracle Database, OOPs, Jscript, HTML)": "https://github.com/smritibharti870/ABC-BANK-FULLSTACK",
    "🏆 Student Management system - By Using Django, MySQL, HTML, CSS, Python":"College Project",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
    
#--- Load CSS, PDF & PROFILE PIC ---

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 9 Months expereince in Diamondpick company as a consultant.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Build a successful "Student Management System" Project in Last Year of my College Project, in this project my resposibities is to lead a team and involve in presentation .
"""
)    

# --- EDUCATION ---
st.write('\n')
st.subheader("EDUCATION")
st.write(
    """
- 👩‍💻 Ramgovind Institute of Technology, Koderma — B.Tech
- 👩‍💻 CH+2 High School, Koderma — Intermediate
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Matplotlib, Pandas), SQL
- 📊 Data Visulization: MS Excel
- 📚 Framework: Django
- 🗄️ Databases: MySQL
"""
)

# --- COURSES ---
st.write('\n')
st.subheader("COURSES")
st.write(
    """
- 👩‍💻 Full Stack Developer-J Spider
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Consultant | Diamondpick**")
st.write("03/2022 - 11/2022")
st.write(
    """
- ► Used Embedded C and Linux to Worked to ensure successful project execution according to established objectives, timelines, and costs.
- ► Under-on traning in Embedded C &  Linux.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

    
# --- LANGUAGES ---
st.write('\n')
st.subheader("LANGUAGES")
st.write(
    """
📚English, Hindi
"""
)   

# --- HOBBIES ---
st.write('\n')
st.subheader("HOBBIES")
st.write(
    """
🎤 Singing 

🍽️ Cooking
"""
)   

