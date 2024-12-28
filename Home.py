import streamlit as st
from st_pages import hide_pages, add_page_title, get_nav_from_toml
from streamlit_extras.let_it_rain import rain 
import toml

#Configure Page
#st.set_page_config(page_title="My Protein Is Broken!", page_icon=":dna:", layout="wide")
#st.set_page_config(layout="wide")

nav = get_nav_from_toml(".streamlit/pages.toml")
pg = st.navigation(nav)
pg.run()

#hide_pages(["Transcription", "Identify Mutations", "Translation", "Sandbox Instructions"])




