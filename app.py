import streamlit as st
import os
from bs4 import BeautifulSoup
from streamlit.components.v1 import html as st_html

# Helper for HTML parsing
def extract_profile_info(html_path):
    info = {
        'name': '', 'major_grad': '', 'student_id': '', 'status': '', 'about': '',
        'skills': [], 'email': '', 'image': ''
    }
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        header = soup.find('div', class_='profile-header')
        if header:
            info['image'] = header.find('img')['src']
            info['name'] = header.find('h1').text.strip()
            info['major_grad'] = header.find_all('p')[0].text.strip()
            status_line = header.find_all('p')[1].text
            parts = status_line.split('Student ID:')[-1].split('|')
            info['student_id'] = parts[0].replace(':','').strip()
            if len(parts) > 1:
                status = parts[1].split(':')[-1].strip()
                info['status'] = status.replace('Status:','').replace('Active','Active').replace('</span>','').strip()
        about = soup.find('h2', text='About Me')
        if about:
            info['about'] = about.find_next('p').text.strip()
        skills_div = soup.find('div', class_='skills-list')
        if skills_div:
            info['skills'] = [s.text for s in skills_div.find_all('span', class_='skill-tag')]
        email = soup.find('a', href=lambda h: h and h.startswith('mailto:'))
        if email:
            info['email'] = email.text.strip()
    return info

pages = {
    "Profile": "profile.html",
    "Courses": "courses.html",
    "Announcements": "announcement.html",
    "Grades": "grades.html",
    "Schedule": "schedule.html",
}

st.sidebar.title("Student Portal Navigation")
selected = st.sidebar.radio("Go to", list(pages.keys()))

if selected == "Profile":
    profile_data = extract_profile_info('profile.html')
    st.header("Profile Information")
    with st.form("profile_form"):
        name = st.text_input("Name", profile_data['name'])
        major_grad = st.text_input("Degree | Graduation", profile_data['major_grad'])
        student_id = st.text_input("Student ID", profile_data['student_id'])
        status = st.text_input("Status", profile_data['status'])
        about = st.text_area("About Me", profile_data['about'])
        skills = st.text_input("Skills (comma separated)", ', '.join(profile_data['skills']))
        email = st.text_input("Email", profile_data['email'])
        uploaded_image = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
        submitted = st.form_submit_button("Save Profile")
        if submitted:
            st.success(f"Profile updated for {name}")
            st.write({"Name":name, "Degree/Grad":major_grad, "ID":student_id, "Status":status,
                     "About":about, "Skills":skills, "Email":email, "Image":uploaded_image})
    # Show current profile image
    if os.path.exists(profile_data['image']):
        st.image(profile_data['image'], width=120)

elif selected == "Courses":
    st.header("Courses Offered")
    st.info("[Interactive table and add/edit form coming soon]")

elif selected == "Grades":
    st.header("Your Grades")
    st.info("[Interactive grades table and edit/add form coming soon]")

elif selected == "Announcements":
    st.header("Announcements to Students")
    st.info("[Interactive announcement board and add form coming soon]")

elif selected == "Schedule":
    st.header("Schedule")
    st.info("[Display and editing coming soon]")
