import streamlit as st
import pandas as pd
from st_pages import Page, show_pages, add_page_title, hide_pages
import time
from st_pages import Page, Section, show_pages, add_page_title

st.set_page_config(page_title="Protein Game", page_icon=":dna:", layout="wide")
hide_pages(["Transcription", "Identify Mutations", "Translation", "Sandbox Instructions"])
add_page_title()
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                    padding-right: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)
# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("Home.py", "Home"),
        Page("pages//Sandbox.py", "Sandbox"),
        Page("pages//Sandbox_instructions.py", "Sandbox Instructions"),
        Page("pages//Practice.py", "Mutations Practice"),
        Page("pages//Transcription.py", "Transcription"),
        Page("pages//Translation.py", "Translation"),
        Page("pages//MutationQuiz.py", "Identify Mutations")
    ]
)

st.markdown('''Welcome to ‘My Protein is Broken!’''')
url_teacher = "https://docs.google.com/document/d/14zIgoskGYacwCwsGN8mQvRdwzLc7TBYxQ_2MY5g0cag/edit?usp=sharing"
url_student = "https://docs.google.com/document/d/1HTCqOur0ZR2f5Wvn18qWMzd7jZ9MobXrmC9aUUw5jZE/edit?usp=sharing"
url_feedback = "https://forms.gle/q9mjvDEk1PeHW5aTA"
st.markdown('''For the full teacher instructions, please click [here](%s)!''' % url_teacher)  
st.markdown('''For the full student instructions, please click [here](%s)!''' % url_student)  
st.markdown('''After using this website, please let us know how you liked it [here](%s)!''' % url_feedback)





