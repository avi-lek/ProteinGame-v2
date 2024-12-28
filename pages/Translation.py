from st_pages import hide_pages
import streamlit as st
from practice_functions import *
st.set_page_config(page_title="My Protein Is Broken!", page_icon=":dna:", layout="wide")
#hide_pages(["Transcription", "Identify Mutations", "Translation", "Sandbox Instructions"])
if "translate_win" not in st.session_state:
    st.session_state["translate_win"] = False

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1.5rem;
                    padding-bottom: 1rem;
                    padding-left: 1rem;
                    padding-right: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

translation()