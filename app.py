import os
from streamlit.components.v1 import html

# Mapping of display names to HTML file paths
pages = {
    "Profile": "profile.html",
    "Courses": "courses.html",
    "Announcements": "announcement.html",
    "Grades": "grades.html",
    "Schedule": "schedule.html",
}

st.sidebar.title("Student Portal Navigation")
selected = st.sidebar.radio("Go to", list(pages.keys()))

html_file = pages[selected]
if os.path.exists(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    html(html_content, height=800, scrolling=True)
else:
    st.error(f"The file {html_file} was not found.")
import streamlit as st
import io
import sys

st.title("Python Code Runner")

code = st.text_area("Type your Python code here:", height=200)
run_button = st.button("Run Code")

if run_button:
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    try:
        exec(code, {})
    except Exception as e:
        st.error(f"Error: {e}")
    sys.stdout = old_stdout
    output = redirected_output.getvalue()
    st.text_area("Output:", output, height=200)